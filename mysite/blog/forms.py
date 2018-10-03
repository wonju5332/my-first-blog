from django import forms
from .models import Post

class PostForm(forms.ModelForm): # PostForm 은 우리가 만들 폼의 이름이며, 장고에게 인식시켜주기 위해 넣어줌
    class Meta: # 어떤 모델을 쓸 것인지 알려주는 클래스.
        model = Post
        fields = ('title', 'text', )
