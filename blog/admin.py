from django.contrib import admin
from .models import Blog, Category, ContactFormResponse, Comment
# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(ContactFormResponse)
admin.site.register(Comment)
