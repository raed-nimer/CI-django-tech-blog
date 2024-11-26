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

def loginView(request):
    # On Logging in
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Authentcating User
        user = authenticate(request, username=username, password=password)
        # if user details were correct
        if user is not None:
            # login the user
            login(request, user)
            return redirect('home')
         
        
    return render(request, 'accounts/login.html')
