from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse

User = get_user_model()


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        # posts value는 QuerySet
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


# post_detail 기능 함수 구현
# 'post'라는 key로 Post.objects.first()에 해당하는 객체를 전달
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


def post_add(request):
    # post 생성 완료 후(DB에 저장 후), post_list 페이지로 돌아가기
    # https://docs.djangoproject.com/ko/1.11/topics/http/shortcuts/#redirect
    # extra) 작성한 post에 해당하는 post_detail 페이지로 이동
    #
    # post 생성 시 Post.objects.create() 메서드 사용
    #
    # extra) Post delete기능 구현
    # def post_delete(request, pk):
    #   (POST 요청에서만 동작해야함)
    #   ->pk에 해당하는 post를 삭제하고, post_list페이지로 이동

    if request.method == 'POST' and request.POST.get('title') and request.POST.get('content'):
        title = request.POST['title']
        content = request.POST['content']

        author = User.objects.get(username='sejun')
        post = Post.objects.create(author=author, title=title, content=content)
        #post = Post(author=author, title=title, content=content)
        if request.POST.get('publish'):
            post.publish()
        else:
            post.save()
        return redirect('post_detail', pk=post.pk)
    else:
        context = {

        }
    return render(request, 'blog/post_form.html', context)
