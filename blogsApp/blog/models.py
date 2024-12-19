from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200) # required
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)

class Blog(models.Model):
    title = models.CharField(max_length=100) # string - required
    # description = models.TextField(null=True, blank=True) # description is optional
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='images/default.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User Connection
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)   # category id
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # Update 'updated_at' everytime the data updates.

    def __str__(self):
        return str(self.title)
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # User Connection
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # Update 'updated_at' everytime the data updates.
    
class ContactFormResponse(models.Model):
    name = models.CharField(max_length=100) # string - required
    email = models.CharField(max_length=100) # string - required
    subject = models.CharField(max_length=100) # string - required
    description = models.TextField(null=True, blank=True) # description is optional 
    
    def __str__(self):
        return str(self.name)