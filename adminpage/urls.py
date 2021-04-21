from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.AdminHome, name='adminhome'),
    path('login', views.AdminLogin, name='adminlogin'),
    path('logout', views.AdminLogout, name='adminlogout'),

    path('user-create', AdminUserCreate.as_view(), name='usercreate'),
    # path('user-edit/<int:pk>', views.AdminUserEdit, name='useredit'),
    path('user-edit/<int:pk>', AdminUserEdit.as_view(), name='useredit'),
    path('user-delete/<int:pk>', AdminUserDelete.as_view(), name='userdelete'),
    # path('user-search/<int:pk>', views.AdminUserSearch, name='usersearch'),
]
