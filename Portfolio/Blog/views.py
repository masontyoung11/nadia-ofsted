from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from spotlight.models import Categories
from .models import Post

# Create your views here.
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            print("failed")
            print(username)
            return redirect('blog')

    return render(request, 'signin.html', {'categories': Categories.objects.all()})


def signout(request):
    logout(request)
    
    return redirect('blog')

@login_required
def dashboard(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        for letter in title:
            if letter == ' ':
                search_title = title.replace(letter, '-')

        if Post.objects.filter(title=title):
            return redirect('blog')
        else:
            Post.objects.create(title=title, content=content, search_title=search_title)


    if not request.user.is_authenticated and not request.user.is_superuser:
        return redirect('blog')
    else:
        return render(request, 'dashboard.html', {'categories': Categories.objects.all()})