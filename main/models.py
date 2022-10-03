from distutils.command.upload import upload
from doctest import register_optionflag
import email
from importlib.util import module_for_loader
from itertools import product
from multiprocessing.spawn import old_main_modules
from unicodedata import category
from django.db import models
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User,AbstractUser

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
    client = models.ForeignKey(User,on_delete=models.CASCADE,related_name='shop_client')
    date =models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    def __str__(self):
        return str(self.client)
    
   
    

class ShopItems(models.Model):
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE,related_name='item_savatcha')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='item_product')
    quantity = models.IntegerField()
    totalPay = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)
    
    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity * self.product.price)

    @property
    def varamount(self):
        return (self.quantity + self.product.price)
    
    
    
    @property
    def get_total(self):
        if self.product.discount:
            total = self.product.price * ((100-self.product.discount)/100)
        else:
            total = self.product.price * self.quantity
        
        return total
    @property
    def Totalget(self):

        self.shop.total += self.totalPay
        return self.shop.total
    


    # class Register(models.Model):
    #     userna

class Contact(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    text = models.TextField()   
    def __str__(self):
        return self.full_name

class Shipping(models.Model):
  
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    region = models.CharField( max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    zipcode = models.IntegerField()
    phone = models.IntegerField()
    def __str__(self):
        return self.first_name
    
  
    

      
    
        