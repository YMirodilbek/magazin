from pyexpat import model
from django.forms import EmailField, ModelForm
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import Email

from .models import *

class CreateUserForm(UserCreationForm):
    email=EmailField()
    class Meta:
        model= User
        fields = ['username','tel','password1','password2']


