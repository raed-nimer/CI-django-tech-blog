from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),  # /
    path('blogs/<str:pk>/', views.blogDetails, name="details"),
    path('add-blog/', views.addBlog, name="add-blog"),
    path('blogs/<str:pk>/update', views.updateBlog, name="update-blog"),
    path('blogs/<str:pk>/delete', views.deleteBlog, name="delete-blog"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),  # route for contact page
    path('search/', views.searchBlogs, name="search"),  # search blogs
]

urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
