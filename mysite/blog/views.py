from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # 쿼리셋의 이름.
    return render(request, 'blog/post_list.html', {'posts' : posts } ) # 템플릿을 사용하기 위해 매개변수를 추가. {} 부분 즉, posts변수를 템플릿에 넘겨줌.





# Create your views here.
