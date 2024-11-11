from django.shortcuts import render
from .models import Blog
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
    return render(request, 'blog/contact.html')

def blogDetails(request, pk):
    blog = Blog.objects.get(id=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blogDetails.html', context)