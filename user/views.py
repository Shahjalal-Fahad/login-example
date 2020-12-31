from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
 

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already taken")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password1,email=email)
                user.save()
                return redirect("login")

    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,"invalid credentials")
            return redirect("login")

    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')