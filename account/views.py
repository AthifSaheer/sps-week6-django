from django.shortcuts import render, redirect
from django.views.generic import *
from.forms import UserRegistrationForm, UserLoginForm
from .models import Customer
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


class HomeView(TemplateView):
    template_name = 'home.html'

class RegistrationView(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        email  = form.cleaned_data.get('email')
        if password1 == password2:
            print("user succesfully created")
            user = User.objects.create_user(username, password1, email)
        else:
            # messages.error(form, "Password did not match")
            print("password did not match")
            return redirect('register')
        form.instance.user = user
        login(self.request, user)
        return super().form_valid(form)


class LoginView(FormView):
    template_name = 'login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')

    #form_valid method is a type of post methd and is available in CreateView, FormView and UpdateView
    def form_valid(self, form):
        uname = form.cleaned_data.get('username')
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and usr.customer:
            login(self.request, usr)
            print("user login successfull")
        else:
            print("Invalid creditials ! !")
            return render(self.request, self.template_name, {"form":self.form_class, "error":"Invalid creditials ! !"})
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
