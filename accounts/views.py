from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        #Get form values
        first_name = request.POST['first_name']
        first_name = request.POST['last_name']
        first_name = request.POST['username']
        first_name = request.POST['email']
        first_name = request.POST['password']
        first_name = request.POST['password2']
    else:
        return render(request, 'apps/accounts/register.html')

def login(request):
    return render(request, 'apps/accounts/login.html')

def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'apps/accounts/dashboard.html')
