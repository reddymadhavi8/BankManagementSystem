from django.urls import path

from Studentmarksapp import views

urlpatterns=[
    path('',views.home),
    path('displaystudent',views.displaystu_fun,name='displaystudent'),
    path('addstudent',views.addstu_fun,name='addstudent'),
    path('readstudentdata',views.readstu_fun,name='readstudentdata'),
    path('update/<int:id>',views.update_fun,name='update'),
    path('delete/<int:id>',views.delete_fun,name='delete'),
]