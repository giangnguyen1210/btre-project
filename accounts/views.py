from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        # Register user
        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email is being used')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password, 
                    first_name=first_name, last_name=last_name) 
                    # login after register
                    # auth.login(request,user)
                    # messages.success(request,"you now login ")
                    user.save()
                    messages.success(request,'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request,'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'Successful logged out')
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')