from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name = 'post_list'),
]

# post_list 라는 이름의 view가 ^$ URL에 할당된 것.
#이 REGEX는 ^에서 시작해 $로 끝나는 지 매칭할 것.
# 즉, 문자열이 아무것도 없는 경우만 매칭 할 것.
# 왜냐하면 resolver는 (장고URL확인자)는 URL의 일부가 아니기 때문..
# 그래서 이 패턴은, 장고에게 누군가 웹사이트 127.0.0.1:8000 으로 들어왔을 때, view.post_list를 보여주라고 말할 것.

#name = 'post_list'는 뷰를 식별할 수 있도록 하는 네임
