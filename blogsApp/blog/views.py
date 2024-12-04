#backend
from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm, ContactFormResponseForm
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
            return redirect('home')
        else:
            print("WE have an error")
    form = ContactFormResponseForm() # CREATING A FORM
    context = {
            'form': form
        }
    return render(request, 'blog/contact.html', context)

# Function responsible for showing the form + adding the blog.
def add_blog(request):
    if request.method == 'POST':
        # request.POST => 
        form = BlogForm(request.POST, request.FILES)
        # Checking if the data is valid or not.
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print("WE have an error")
    
    else:
        form = BlogForm() # CREATING A FORM
        context = {
            'form': form
        }
        return render(request, 'blog/addBlog.html', context)

def blogDetails(request, pk):
    
    blog = Blog.objects.get(id=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blogDetails.html', context)

def update_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    form = BlogForm(instance=blog)
    
    # if update form submitted
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {
        'title': 'Update Blog',
        'form': form
    }
    
    return render(request, 'blog/editBlog.html', context)

def delete_blog(request, pk):
    blog = Blog.objects.get(id=pk)
    blog.delete()
    return redirect('dashboard')