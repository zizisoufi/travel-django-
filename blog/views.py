from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    posts = Paginator(posts,3) 
    try:  
        page_number = request.Get.get('page')
        posts = posts.get_page(page_number)
    except PageNotInteger:
        posts = post.get_page(1)
    except emptyPage:
        posts = posts.get_page(1)    
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post' : post}
    return render(request, 'blog/blog-single.html', context)



def blog_index(request):
    return render(request, 'blog/blog-home.html' )

def blog_category(request):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    #print(request.__dict__)
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        #print(request.GET.get('s'))
        # if s := request.GET.get('s'): #use this method only when your using python version 3.8 and above
        if request.GET.get('s'):
            s =  request.GET.get('s')
            posts = posts.filter(content__contains=s)
    
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)
