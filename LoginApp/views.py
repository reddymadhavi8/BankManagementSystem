from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    return render(request,'home.html')


def loginfun(request):
    return render(request,'login.html')


def registerfun(request):
    return render(request,'register.html')


def readregister_fun(request):
    username = request.POST['tbtext']
    email = request.POST['tbemail']
    password = request.POST['tbpwd']

    user = User.objects.create_superuser(username=username, email=email, password=password)
    user.save()
    return render(request, 'login.html', {'msg': f' user created successfully'})




def readloginfun(request):
    username = request.POST['tbuser']
    password = request.POST['tbpwd']
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        return redirect('displaystudent')
    else:
        return render(request, 'login.html')


def logout_fun(request):
    logout (request)
    return redirect('login')