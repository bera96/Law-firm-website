
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q




def post_index(request):
    posts = Post.objects.all()
    query = request.GET.get('query')
    if query:
        posts = posts.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)

        ).distinct()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj,
    }
    return render(request, 'post/index.html',context)




def post_detail(request,slug):

    post = get_object_or_404(Post,slug=slug)
    print(post.id)
    older_post = Post.objects.filter(id=(post.id-1)) 
    if older_post:
        older_post = older_post[0]
    newer_post = Post.objects.filter(id=(post.id+1))
    if newer_post:
        newer_post = newer_post[0]

    context = {
        'post':post,
        'older_post':older_post,
        'newer_post':newer_post
    }
    return render(request, 'post/detail.html',context)



