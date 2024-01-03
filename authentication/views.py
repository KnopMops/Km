from django.contrib.auth import authenticate, login as dj_login, logout
from django.shortcuts import render, redirect

from .models import User


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if name and email and password1 and password2:
            if password1 == password2:
                user = User.objects.create_user(name, email, password1)
                return redirect('login')

    return render(request, 'authentication/signup.html')


def logout_from_account(request):
    logout(request)
    return redirect('home')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        if email and password:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                dj_login(request, user)
                return redirect('home')

    return render(request, 'authentication/login.html')