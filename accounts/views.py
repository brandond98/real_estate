from django.shortcuts import render, redirect

def register(request):
    return render(request, 'apps/accounts/register.html')

def login(request):
    return render(request, 'apps/accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'apps/accounts/dashboard.html')
