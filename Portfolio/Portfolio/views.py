from django.shortcuts import render, get_object_or_404
from spotlight.models import Categories
from Blog.models import Post

def index(request):
    return render(request, 'index.html', {'categories': Categories.objects.all()})


def post(request, blog_post):
    print(blog_post)
    post = get_object_or_404(Post, search_title = blog_post)

    return render(request, 'post.html', {'post': post, 'replies': post.comments, 'categories': Categories.objects.all()})

def blog(request):
    return render(request, 'blog.html', {'categories': Categories.objects.all(), 'posts': Post.objects.all()})