from django.shortcuts import render

from django.http import HttpResponse
from . import urls

def index(request):
    return HttpResponse("Hello, world. You're at the tournaments index.")
