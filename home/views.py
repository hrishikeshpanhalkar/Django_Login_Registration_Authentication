

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
    return render(request, "home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print("username: " + username + " passsword: " + password)
        if username == "" or password == "":
            messages.info(request, "Please Fill All the Details!!")
            return redirect('login')
        else:
            user = auth.authenticate(username=username, password=password)
        
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Invalid UserName or Password")
                return redirect("login")        
    else:
        return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print(username + " " + password + " " + first_name + " " + last_name + " " + email)
        if password == confirm_password:
            print("hello")
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username is already exist!!")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.set_password(password)
                user.save()
                return redirect('/')
    else:
        return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect("/")