from django.urls import path
from . import views

app_name = 'admins'


urlpatterns = [
     
    path('admin-home', views.AdminHomePage, name='admin-home'),
    path('user-list-view', views.UserListView, name='user-list-view'),
    path('admin-logout', views.AdminLogout,  name='admin-logout'),
    path('useractivate/<int:pk>/', views.ActivateUser, name='useractivate'),
    path('deactivateuser/<int:pk>/', views.DeactivteUser, name='deactivateuser'),
]