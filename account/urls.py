from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('register', RegistrationView.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
