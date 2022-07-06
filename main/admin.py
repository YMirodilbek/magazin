from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(ShopItems)
admin.site.register(Contact)




