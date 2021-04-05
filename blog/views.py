# 애플리케이션의 logic을 넣는 곳
# 모델에서 필요한 정보를 받아와 템플릿에 전달
from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
