from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.core.exceptions import ValidationError
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'home/homepage.html')

def profile(request):
    return render(request, 'accounts/profile.html')
    

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']

            if User.objects.filter(username=username).exists():
                form.add_error('username','This username already exists.')

            if User.objects.filter(email=email).exists():
                form.add_error('email','This email is already registered. Reset password?')

            if not form.errors:
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/userMgmt')    

    else:
        form = UserRegistrationForm()
        
    return render(request, 'registration/register.html', {'form': form})


