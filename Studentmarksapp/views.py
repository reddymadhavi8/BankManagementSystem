from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Studentmarksapp.models import Student, Course, City


# Create your views here.
@login_required
def home(request):
    return redirect('displaystudent')

@login_required
def displaystu_fun(request):
    return render(request,'displaystudent.html',{'Student':Student.objects.all()})

@login_required
def addstu_fun(request):
    cities=City.objects.all()
    courses=Course.objects.all()
    return render(request,'addstudent.html',{'cities':cities,'courses':courses})


def readstu_fun(request):
    s=Student()
    s.Fname=request.POST['tbfname']
    s.Lname = request.POST['tblname']
    s.Email = request.POST['tbemail']
    s.Mobileno = request.POST['tbnum']
    s.Course = Course.objects.get(course_name=request.POST["ddlcourse"])
    s.City = City.objects.get(city_name=request.POST["ddlcity"])
    s.save()
    return redirect('displaystudent')


def update_fun(request,id):
    cities = City.objects.all()
    courses = Course.objects.all()
    s = Student.objects.get(id=id)
    if request.method == 'POST':
        s.Fname = request.POST["tbfname"]
        s.Lname = request.POST["tblname"]
        s.Mobileno = int(request.POST["tbnum"])
        s.Email = (request.POST["tbemail"])
        s.Course = Course.objects.get(course_name=request.POST["ddlcourse"])
        s.City = City.objects.get(city_name=request.POST["ddlcity"])
        s.save()
        return redirect('displaystudent')

    return render(request, 'updatestudent.html', {'data': s, 'cities': cities, 'courses': courses})



def delete_fun(request,id):
    s = Student.objects.get(id=id)
    s.delete()
    return redirect('displaystudent')
