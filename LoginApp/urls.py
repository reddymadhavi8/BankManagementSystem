from django.urls import path

from LoginApp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.loginfun,name='login'),
    path('register',views.registerfun,name='register'),
    path('readregister',views.readregister_fun,name='readregister'),
    path('readlogin',views.readloginfun,name='readlogin'),
    path('logout',views.logout_fun,name='logout'),



]