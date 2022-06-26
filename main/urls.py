from django.urls import path,include
from .views import *


urlpatterns = [
    path('', Home),
    path('product-detail/<int:pk>', ProductDetail.as_view()),
    path('add_cart/<int:id>/', AddToCart),
    path('categ/<int:id>/', CategoryFilter),
    path('cart/',Cart),
    path('count/',CountSavatcha),
    path('delete-cart/<int:id>',DeleteCart),
    path('login/',Login),
    path('register/',Register),

 ]
 