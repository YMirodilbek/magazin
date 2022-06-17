from django.shortcuts import render
from .urls import *
# Create your views here.


def Home(request):
    return render(request,'home.html')