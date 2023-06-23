from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth import logout
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    context={
        'posts':posts
    }
    return render(request, 'post_list.html', context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list') 
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('create_post')  
    else:
        form = LoginForm()
    
    return render(request, 'user_login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')