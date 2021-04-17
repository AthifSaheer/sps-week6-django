from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
]
