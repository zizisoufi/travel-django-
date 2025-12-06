from django import template
from blog.models import Post, Category

# اینجا باید L بزرگ باشه
register = template.Library()

@register.inclusion_tag('blog/popular-posts.html')
def latestposts():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:1]  # آخرین پست
    return {'posts': posts}

@register.inclusion_tag('blog/post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}
