# 장고 함수인 path와, blog app에서 사용할 모든 view를 가져옴 
from django.urls import path
from . import views

urlpatterns=[
    # post_list라는 view가 루트 URL에 할당
    # 8000/ 주소로 들어왔을 때 views.post_list를 보여주라 말해줌
    # name='post_list'로 URL에 이름 붙인 것으로 뷰를 식별
    path('', views.post_list, name='post_list'),
]