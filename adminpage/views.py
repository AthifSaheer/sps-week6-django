from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import *
from .filters import UserFiler
from account.forms import *
from django.db.models import Q
from django.views.decorators.cache import cache_control


# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
def AdminHome(request):
    if request.session.has_key('is_value'):
        users = User.objects.all()
        search = UserFiler(request.GET, queryset=User.objects.exclude(is_staff=1))
        context = {'users':users, 'search':search}
        return render(request, 'admintemplate/home.html', context)
    return redirect('adminlogin')


def AdminLogin(request):

    if request.session.has_key('is_value'):
        return render(request, 'admintemplate/home.html')

    if request.method == 'POST':
        username = 'admin'
        password = 'admin'
        
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        if username == uname and password == pword:
            request.session['is_value'] = True
            print("login succesfull")
            return redirect('adminhome')
        else:
            # messages.info(request, "Invalide creditials")
            error = "Invalide creditials"
            return render(request, 'admintemplate/login.html', {'error':error})
            # print(error)
            # if username == uname and password == pword:
            #     print('---------')
    else:
        return render(request, 'admintemplate/login.html')


def AdminLogout(request):
    del request.session['is_value']
    return redirect('adminlogin')

class AdminUserCreate(CreateView):

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'admintemplate/usercreate.html', {'form':form})

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if password == password_confirmation:
            print("user succesfully created")
            user = User.objects.create_user(username, email, password_confirmation)
            # user = request.save(commit=False)
            # user.save()
            return redirect('adminhome')
        else:
            print("password did not match")
            return redirect('usercreate')
        return redirect('usercreate') 

class AdminUserEdit(UpdateView):
    template_name = "admintemplate/useredit.html"
    form_class = UserRegistrationFormForAdmin
    # get_object_name = "adminhome1"
    model = User
    success_url = 'adminhome'

    def get_success_url(self):
        return reverse_lazy('adminhome')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AdminUserDelete(DeleteView):
    template_name = "admintemplate/userdelete.html"
    model = User
    success_url = "/adminpage"

