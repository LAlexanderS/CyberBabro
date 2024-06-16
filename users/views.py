# views.py
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ProfileForm, UserLoginForm, UserRegistrationForm
from .models import User
from personal.models import Personal
from main.models import Personalapplication
def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    
    context = {
        "title": "Авторизация",
        'form': form,
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
    
    context = {
        "title": "Регистрация",
        'form': form,
    }
    return render(request, 'users/registration.html', context)

@login_required
def profile(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)
        
    # Получение роли пользователя
    role_s = request.user.role

    # Получение активных заявок для текущего пользователя
    x = request.user.id_s
    
    active_applications = Personalapplication.objects.filter(person=request.user.id_s)

    context = {
        "title": "Профиль",
        'form': form,
        'role_s': role_s,
        'active_applications': active_applications,
        'x': x,
    }
    return render(request, 'users/profile.html', context)

@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))
