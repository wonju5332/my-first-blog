from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # 쿼리셋의 이름.
    return render(request, 'blog/post_list.html', {'posts' : posts } ) # 템플릿을 사용하기 위해 매개변수를 추가. {} 부분 즉, posts변수를 템플릿에 넘겨줌.

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'blog/post_detail.html', {'post' : post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # 넘겨진 데이터를 바로 저장하지 말라. 작성자를 추가한 후 저장할 것.
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form' : form})

def post_edit(request, pk):
    '''

    :param request:
    :param pk: url로부터 pk 매개변수를 받아 처리한다.
    :return:

    get_object_or_404 를 호출하여 수정하고자 하는 글의 Post 모델 인스턴스로 가져온다.
    즉, 수정 전의 데이터와 수정반영하고자 하는 데이터를 가지고 있어야 하는 상황이므로.
    '''
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


# New post 작성 시, request.POST가 데이터를 가지고 있음.
# POST는, "글"의 의미가 아닌, Posting한다는 개념.
# form.is_valid() 는 값이 올바른지 확인하는 메소드
# Create your views here.
