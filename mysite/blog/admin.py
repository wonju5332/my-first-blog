from django.contrib import admin
from .models import Post

admin.site.register(Post) # 관리자 페이지에서, 모델을 보려면 admin.site.register(Post)로 모델을 등록한다.
