from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.home, name="home"), # /
    path('blogs/<str:pk>/', views.blogDetails, name="details"),
    path('about/', views.about, name="about"), # route
    path('contact/', views.contact, name="contact") # route for contact page
]