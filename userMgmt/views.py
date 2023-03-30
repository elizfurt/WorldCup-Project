from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm
from django.core.exceptions import ValidationError
from django.contrib import messages
from .context_processors import user_dashboard
from tournament.models import Resultz, Tournament_song
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

def index(request):
    return render(request, 'home/homepage.html')

def userDashboard(request):
    ranking_html = render_to_string('ranking_html.html')
    context = {
        'ranking_html': ranking_html,
        'user_dashboard': user_dashboard
    }
    return render(request, 'accounts/userDashboard.html', context)
    
def register(request, email=''):
    email = request.GET.get('email', '')
    if email:
        form = UserRegistrationForm(initial={'email': email})
    else:
        form = UserRegistrationForm()

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

    return render(request, 'registration/register.html', {'form': form})

def userDashboard(request):
    rankings = Resultz.objects.order_by('-points')
    ranking_html = render_to_string('ranking_html.html', {'rankings': rankings})
    context = {
        'ranking_html': ranking_html,
        'user_dashboard': user_dashboard
    }
    return render(request, 'accounts/userDashboard.html', context)