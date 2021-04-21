from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control, never_cache
from.forms import UserRegistrationForm, UserLoginForm
from django.utils.decorators import method_decorator
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import *


# @login_required(login_url='login')
def HomeView(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')
    

class RegistrationView(CreateView):

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form':form})

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if password == password_confirmation:
            print("user succesfully created")
            user = User.objects.create_user(username, email, password_confirmation)
            login(request, user)
            return redirect('home')
        else:
            form = UserRegistrationForm()
            pwrd_error = "password did not match"
            print(pwrd_error)
            return render(request, 'register.html', {'pword_error':pwrd_error, 'form':form})
        # return redirect('register')


class Login(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserLoginForm()
            return render(request, 'login.html', {'form':form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(request, username=username, password=password)
        print(usr)

        if usr is not None:
            login(request, usr)
            return redirect('home')
        else:
            error = 'Invalid creditials ! !'
            print(error)
            form = UserLoginForm()
            return render(request, 'login.html', {'error':error, 'form':form})
        
        


def LogoutView(request):
    logout(request)
    request.session['is_value'] = True
    return redirect('login')


