from django.conf import settings
from django.db import models
from django.utils import timezone

#models.때문에 장고는 Post가 db에 저장되어야 한다고 알게됨
class Post(models.Model):
    
    # 다른 모델에 대한 링크
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    #CharField : 글자 수가 제한된 텍스트를 정의할 때
    title = models.CharField(max_length=200)

    #TextField : 글자 수가 무제한. 블로그 콘텐츠...
    text = models.TextField()

    #DateTimeField : 날짜와 시간
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title