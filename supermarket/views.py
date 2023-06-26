from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello, world!')

# chacha kaise ho 

def login(request):
    return HttpResponse('kaise ho chacha')