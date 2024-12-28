from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from blog.models import Blog
from django.contrib import messages
from .forms import RegisterUserForm, UpdateUserForm, LoginForm
# Create your views here.
def registerView(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Take the user to home page
            return redirect('home')
    
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

def loginView(request):
    # On Logging in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Authentcating User
        user = authenticate(request, username=username, password=password)
        # if user details were correct
        if user is not None:
            # login the user
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid username or password')
            return redirect('login')
         
    return render(request, 'accounts/login.html')
    
def logoutView(request):
    logout(request)
    return redirect('home')

# Check to authenticate user
@login_required(login_url='login')
def dashboardView(request):
    # dynamic data
    paginator = Paginator(Blog.objects.filter(user=request.user), 5)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)
    
    context = {
        'blogs': blogs
    }
    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def profileView(request):
    form= UpdateUserForm(instance=request.user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect("profile")
    context = {
        'form': form 
    }
    return render(request, 'accounts/profile.html', context)
    