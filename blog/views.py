# 애플리케이션의 logic을 넣는 곳
# 모델에서 필요한 정보를 받아와 템플릿에 전달
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# models.py에 정의된 모델을 가져올 것
from .models import Post



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