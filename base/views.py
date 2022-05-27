from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import BlogForm, UserForm
from .models import Blog, Message
from django.contrib.auth.decorators import login_required


# from django.contrib.http import redirect

def loginuser(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = UserForm.objects.get(username=username)
        
        except:
            messages.error(request, "user does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "theres a problem with log in")


    context = {"page": page}
    return render(request, 'base/login_register.html', context)


def logoutuser(request):
    logout(request)
    return redirect("home")


def Register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)

            return redirect('home')

    context = {'form': form}
    return render(request, 'base/login_register.html', context)



def home(request):
    blogs = Blog.objects.all()
    
    context = {'blogs': blogs}
    return render(request, 'base/home.html', context)

    class Meta:
        ordering = ['-created']

def about(request):
    return render(request, 'base/about.html')

@login_required(login_url='login')
def create(request):
    # blogs = Blog.objects.all()
    form = BlogForm()
    # blogs = Blog.objects.all()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blogs = form.save(commit=False)
            blogs.owner = request.user
            blogs.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/add.html', context)


def blogpost(request, pk):
    blogs = Blog.objects.get(id=pk)
    messages =  blogs.message_set.all()

    if request.method == 'POST':
        Message.objects.create(
            owner = request.user,
            blogs = blogs,
            body = request.POST.get('body')
        )

        return redirect('blogpost', pk=blogs.id)
    

    context = {'blogs': blogs, 'messages': messages}
    return render(request, 'base/details.html', context)
