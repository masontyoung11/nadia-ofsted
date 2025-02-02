from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from spotlight.models import Categories
from .models import Post, Comment

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog')
        else:
            return redirect('blog')

    return render(request, 'signin.html', {'categories': Categories.objects.all()})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username):
            return redirect('signup')
        else:
            User.objects.create_user(username=username, email=email, password=password)

    return render(request, 'signup.html', {'categories': Categories.objects.all()})


def signout(request):
    logout(request)
    
    return redirect('blog')


@login_required
def dashboard(request):
    if request.method == 'POST' and request.user.is_superuser:
        if request.POST['edit']:
            search_title = request.POST['edit']

            try:
                post = Post.objects.get(search_title=search_title)
                post.title = request.POST['title']
                post.content = request.POST['content']
                search_title = request.POST['title'].replace(' ', '-').lower()
                post.search_title = search_title
                post.save()

                return redirect('post', blog_post=search_title)
            except Post.DoesNotExist:
                return redirect('blog')
            

        else:
            title = request.POST['title']
            content = request.POST['content']

            for letter in title:
                if letter == ' ':
                    search_title = title.replace(letter, '-')

            if Post.objects.filter(title=title):
                return redirect('blog')
            else:
                Post.objects.create(title=title, content=content, search_title=search_title.lower())
    

    if not request.user.is_authenticated or not request.user.is_superuser:
        logout(request)
        return redirect('blog')
    else:
        return render(request, 'dashboard.html', {'categories': Categories.objects.all()})
    

@login_required
def delete_post(request, search_title):
    if request.user.is_superuser:
        try:
            post = Post.objects.get(search_title=search_title)
            post.delete()

            return redirect('blog')
        except Post.DoesNotExist:
            return redirect('blog')
    else:
        logout(request)
        
    return redirect('blog')


@login_required
def edit_post(request, search_title):
    if request.user.is_superuser:
        try:
            post = Post.objects.get(search_title=search_title)
            return render(request, 'dashboard.html', {'categories': Categories.objects.all(), 'post': post})
        except Post.DoesNotExist:
            return redirect('blog')
    else:
        logout(request)
        
        
    return redirect('blog')


@login_required
def make_comment(request):
    if request.method == 'POST':
        post = Post.objects.get(search_title=request.POST['post_id'])
        content = request.POST['reply']

        print(request.user)

        comment = Comment.objects.create(creator=request.user, content=content, post=post)
        post.comments.add(comment)

        return redirect(request.path)

    return redirect('blog')