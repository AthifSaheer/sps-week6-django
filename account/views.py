from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from.forms import UserRegistrationForm, UserLoginForm
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import *


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'home.html'

    # @login_required
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)
    

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
            print("password did not match")
            return redirect('register')
        return redirect('register')    


class Login(View):

    def get(self, request):
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
            print('Invalid creditials ! !')
        return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
