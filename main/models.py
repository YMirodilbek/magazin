from distutils.command.upload import upload
from importlib.util import module_for_loader
from itertools import product
from multiprocessing.spawn import old_main_modules
from unicodedata import category
from django.db import models
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category =  models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='categ/')
    def __str__(self):
        return self.category

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,related_name='Sort')
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='media/')
    price = models.IntegerField()
    discount = models.IntegerField()
    Is_New = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Shop(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    date =models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    def __str__(self):
        return str(self.client)
    

class ShopItems(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField(default=1)
    def __str__(self):
        return str(self.id)
    

    # class Register(models.Model):
    #     userna
        