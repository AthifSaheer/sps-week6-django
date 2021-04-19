from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.AdminHomeView, name='adminhome'),
    path('register', views.AdminRegistrationView, name='adminregister'),
    path('login', views.AdminLoginView, name='adminlogin'),
    path('logout', views.AdminLogoutView, name='adminlogout'),
]
