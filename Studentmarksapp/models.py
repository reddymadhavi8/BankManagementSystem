from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=50)

    def __str__(self):
        return self.city_name

class Course(models.Model):
    course_name = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name

class Student(models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Mobileno = models.BigIntegerField()
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.Fname
from django.db import models

# Create your models here.
