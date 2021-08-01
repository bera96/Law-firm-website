
from django.shortcuts import get_object_or_404, render
from .models import Post




def post_index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'post/index.html',context)




def post_detail(request,slug):

    post = get_object_or_404(Post,slug=slug)

    context = {
        'post':post
    }
    return render(request, 'post/detail.html',context)



