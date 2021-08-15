from urllib.parse import quote_plus
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.core.paginator import Paginator
from django.db.models import Q,F
import json
from django.views.decorators.csrf import csrf_exempt






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
    share_string = quote_plus(post.content)
    older_post = Post.objects.filter(id=(post.id-1)) 
    if older_post:
        older_post = older_post[0]
    newer_post = Post.objects.filter(id=(post.id+1))
    if newer_post:
        newer_post = newer_post[0]

    context = {
        'post':post,
        'older_post':older_post,
        'newer_post':newer_post,
        'share_string':share_string,
    }
    return render(request, 'post/detail.html',context)


@csrf_exempt
def calculate_number_likes(request):

    data = json.loads(request.body)
    id = data['post_id']
    has_liked = request.COOKIES.get(f'has_liked_{id}')
    print("ilk: ",has_liked)


    if has_liked:
        print("has_liked true")
        Post.objects.filter(id=id).update(number_like=F('number_like') -1)
        state=False
    if not has_liked:
        print("has_liked false")
        Post.objects.filter(id=id).update(number_like=F('number_like') +1)
        state = True
   

    content = {'state':state}
    response = JsonResponse(content, status=200)
    response.set_cookie(key="has_liked_" +id, value=state, max_age=3600)

    
    return response



