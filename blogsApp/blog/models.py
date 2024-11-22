from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200) # required
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)

class Blog(models.Model):
    title = models.CharField(max_length=100) # string - required
    description = models.TextField(null=True, blank=True) # description is optional
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    # category
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # Update 'updated_at' everytime the data updates.

    def __str__(self):
        return str(self.title)