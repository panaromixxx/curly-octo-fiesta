from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('profile')
            else:
                return render(request, 'core/sign_in.html')
        else:
            return render(request, 'core/sign_in.html', {'error':'Неверный логин или пароль'})
    return render(request, 'core/sign_in.html')

def profile(request):
    return render(request, 'core/profile.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']
        email = request.POST['email']
        if password == password_repeat and password != '':
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('sign_in')
        else:
            return render(request, 'core/sign_up.html', {'error':'Пароли не совпадают'})
    return render(request, 'core/sign_up.html')

def sign_out(request):
    logout(request)
    return redirect('sign_in')