from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

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
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse('해당 포스트가 존재하지 않습니다.')
    context = {
        'post': post,
    }
    return render(request, 'blog/post_detail.html', context)

