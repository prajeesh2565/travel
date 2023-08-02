from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def registration(request):
    if request.method == 'POST':
        uname=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        pwd=request.POST['password']
        cpwd=request.POST['password1']
        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username already exists")
                # return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"choose another email id")
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pwd)
                user.save()
                print('account created')
                return render('/')
        else:
            messages.info(request,'password does not match')
            return redirect('register')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        uname=request.POST['username']
        pwd=request.POST['password']
        user=auth.authenticate(username=uname,password=pwd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"wrong credentials")
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')