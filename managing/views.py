from django.shortcuts import render
from main.models import *
# Create your views here.

def Index(request,id):
    shop = Shop.objects.get(client=request.user)
    return render(request,'admin/qabul.html')