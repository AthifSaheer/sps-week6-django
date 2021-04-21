from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.HomeView, name="home"),
    path('register', RegistrationView.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', views.LogoutView, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
