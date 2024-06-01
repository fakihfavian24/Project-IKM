from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout  # Rename login
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('login')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')

    username = None
    if request.user.is_authenticated:
        username = request.user.username

    return render(request, 'login.html', {'username': username})
