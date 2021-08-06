
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

    context = {
        'post':post
    }
    return render(request, 'post/detail.html',context)



