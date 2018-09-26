from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200) # 글자수가 제한된 텍스트를 정의할때 사용.ex) 포스트 제목 정의
    text = models.TextField() # 글자수에 제한이 없는 긴 텍스트를 위한 속성. ex) 블로그 콘텐츠
    created_date = models.DateTimeField(
            default=timezone.now) # 날짜와 시간
    published_date = models.DateTimeField(
            blank=True, null=True) # 다른 모델에 대한 링크 의미

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
