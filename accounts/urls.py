from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.Home, name='home' ),
    path('admin-login', views.AdminLoginPage, name='admin-login'),
    path('user-login', views.UserLoginPage, name='user-login'),
    path('user-register', views.UserRegisterPage, name='user-register'),
]