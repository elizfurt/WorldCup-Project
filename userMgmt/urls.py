## userMgmt app
from django.urls import path, include, re_path, reverse
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, userDashboard

from . import views

app_name = 'users'
urlpatterns = [
    # Login page. 
    path('login/', LoginView.as_view(template_name='registration/login.html'),
        name='login'),

    # User Dashboard page 
    re_path(r'^userDashboard/', views.userDashboard, name="userDashboard"),

    # Log-Out page. 
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'),
        name='logout'),

    # Registration Page 
    path('register/', views.register, name='register'),
    path('register/<str:email>/', views.register, name='register'),

    # Profile Page / Index 
    path('', views.index, name='index'),

]