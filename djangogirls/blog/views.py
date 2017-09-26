from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        #posts value는 QuerySet
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)

#post_detail 기능 함수 구현
#'post'라는 key로 Post.objects.first()에 해당하는 객체를 전달
# 템플릿은 blog/post_detail.html을 사용
def post_detail(request):
    context = {
        'post': Post.objects.first()
    }
    return render(request, 'blog/post_detail.html', context)

