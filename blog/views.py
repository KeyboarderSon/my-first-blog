# 애플리케이션의 logic을 넣는 곳
# 모델에서 필요한 정보를 받아와 템플릿에 전달
from django.shortcuts import render, get_object_or_404
# 새 블로그 글 작성 후 post_detail 페이지로 이동하기 위해
from django.shortcuts import redirect
from django.utils import timezone
# models.py에 정의된 모델을 가져올 것
from .models import Post
from .forms import PostForm



# Create your views here.
def post_list(request):
    # QuerySet인 posts
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # posts를 템플릿에 넘겨줌
    return render(request, 'blog/post_list.html', {'posts':posts})

# 새로운 뷰 추가
#
def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

# 새로운 view 추가
def post_new(request):
    if request.method == "POST":
        # 폼에서 받은 데이터를 넘겨줘야겠다
        form = PostForm(request.POST)
        # 폼에 입력된 값이 올바른가
        if form.is_valid():
            # commit=False : 넘겨진 데이터 바로 post 모델에 저장 x~!
            # 작성자 추가해서 저장하려고 일단 false함
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            # 새 블로그 글 작성 후 post_detail 페이지로 이동
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    # 수정하려는 글의 Post model 인스턴스로 가져옴
    # (pk로 원하는 글을 찾음)
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # 폼에서 받은 데이터를 넘겨줘야겠다
        form = PostForm(instance=post)
        # 폼에 입력된 값이 올바른가
        if form.is_valid():
            # commit=False : 넘겨진 데이터 바로 post 모델에 저장 x~!
            # 작성자 추가해서 저장하려고 일단 false함
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            # 새 블로그 글 작성 후 post_detail 페이지로 이동
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
