from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        if User.objects.filter(username=username).exists():
            return redirect('register')
        else:
            user = User.objects.create_user(username=username,password=password,email=email)
            user.save()
            return redirect('login')
    else:
        return render(request,'register.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['pass']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('register')
        else:
            return redirect('login')
    else:
        return render(request,'login.html')
