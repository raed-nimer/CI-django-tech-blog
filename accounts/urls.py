from django.urls import path
from django.http import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.registerView, name="register"),  # register route
    path('login/', views.loginView, name="login"),  # login route
    path('logout/', views.logoutView, name="logout"),  # logout route
    path('dashboard/', views.dashboardView, name="dashboard"),  # Dashboard
    path('profile/', views.profileView, name="profile")  # Dashboard page

]

urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
