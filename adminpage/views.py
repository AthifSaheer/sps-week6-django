from django.shortcuts import render, redirect
from django.views.generic import *
# from.forms import AdminRegistrationForm
from .models import AdminRegistration
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.sessions.models import Session


    # @method_decorator(login_required, name='dispatch')
def AdminHomeView(request):
    # if request.session.has_key('is_value'):
    #     return render(request, 'admintemplate/home.html')
    # return render(request, 'admintemplate/login.html')
    return render(request, 'admintemplate/home.html')


    
def AdminRegistrationView(request):
    
    admin = AdminRegistration.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        print(username, email, confirmpassword)

        if password == confirmpassword:
            # if admin.user_name == username:
            print("User name already exits")
            # else:
            admin_obj = AdminRegistration(user_name=username, email=email, password=password, confrim_password=confirmpassword)
            admin_obj.save()
            return render(request, 'admintemplate/home.html')
        else:
            print("password did not match")
            return render(request, 'admintemplate/register.html')

    return render(request, 'admintemplate/register.html')

def AdminLoginView(request):
    
    username = request.POST.get('username')
    password = request.POST.get('password')

    admin = AdminRegistration.objects.all()
    # pwrod = AdminRegistration.objects.filter(password = password)
    # uname = AdminRegistration.objects.filter(user_name = username)
    admu = username == admin.user_name 
    admp = password == admin.password
    print(admu, admp)
    # print(username,uname, password, pwrod)
    if admu and admp:
        # request.sessions['is_value'] = True
        print("login succesfull")
        return redirect('adminhome')
    else:
        print("Invalide creditials")
    return render(request, 'admintemplate/login.html')


def AdminLogoutView(request):
    del request.sessions['is_value']
    return redirect('adminlogin')


# ===================================== Session ===================================================
