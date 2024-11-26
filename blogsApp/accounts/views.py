from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterUserForm
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
