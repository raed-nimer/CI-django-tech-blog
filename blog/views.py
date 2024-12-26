from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from .models import Blog, Comment
from .forms import BlogForm, ContactFormResponseForm, CommentForm


# Create your views here.
# Contains all our functions
def about(request):
    # calculations
    return render(request, 'blog/about.html')
    #return HttpResponse('This is About Page')

# Function Responsible for managing and rendering home page.
def home(request):
    # Fetching from database
    # DB code
    blogs = Blog.objects.all() # fetching everything from blogs table
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/home.html', context)
    #return HttpResponse('Home Page')

def contact(request):
    if request.method == 'POST':
        # request.POST => 
        form = ContactFormResponseForm(request.POST)
        # Checking if the data is valid or not.
        if form.is_valid():
            form.save()
            # Add a Success Message
            messages.success(request, 'Your contact form has been submitted successfully!')
            return redirect('contact')
       
    form = ContactFormResponseForm() # CREATING A FORM
    context = {
            'form': form
        }
    return render(request, 'blog/contact.html', context)

@login_required(login_url='login')
# Function responsible for showing the form + adding the blog.
def add_blog(request):
    if request.method == 'POST':
        print('User:')
        print(request.user)
        # request.POST => 
        form = BlogForm(request.POST, request.FILES)
        # Checking if the data is valid or not.
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            # Add a Success Message
            messages.success(request, 'Blog created successfully!')
            return redirect('dashboard')
        
    
    else:
        form = BlogForm() # CREATING A FORM
        context = {
            'form': form
        }
        return render(request, 'blog/addBlog.html', context)

# View to show blog details
def blogDetails(request, pk):
    
    # if the request is POST
    if request.method == 'POST':
        form = CommentForm(request.POST)
        # Checking form validity
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = Blog.objects.get(id=pk)
            comment.save()
            return redirect(reverse('details', kwargs={'pk': pk}))
            
            
    blog = Blog.objects.get(id=pk)
    form = CommentForm()
    context = {
        'blog': blog,
        'form': form
    }
    return render(request, 'blog/blogDetails.html', context)

@login_required(login_url='login')
def update_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    
    # if update form submitted
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            # Add a Success Message
            messages.success(request, 'Blog updated successfully!')
            return redirect('dashboard')
    
    context = {
        'title': 'Update Blog',
        'form': form
    }
    
    return render(request, 'blog/editBlog.html', context)

@login_required(login_url='login')
def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    if request.method == 'POST':
        blog.delete()
        # Add a Success Message
        messages.success(request, 'Blog deleted successfully!')
        return redirect('dashboard')
    context = {
        'blog': blog
    }
    return render(request, 'blog/deleteBlog.html', context)

# View to search blogs
def searchBlogs(request):
    query = request.GET.get("q")
    if(query):
        blogs = Blog.objects.filter(title__icontains=query)
        # | Q(description_icontains=query)
    else:
        blogs = Blog.objects.all()
    
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/home.html', context)