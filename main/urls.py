from django.urls import path,include
from .views import *
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('', Home),
    path('product-detail/<int:pk>', ProductDetail.as_view()),
    path('add_cart/', AddToCart),
    path('categ/<int:id>/', CategoryFilter),
    path('cart/',Cart),
    # path('checkout/',CheckOut),
    # path('checkit/',CheckIt),
    # path('count/',CountSavatcha),
    path('delete-cart/<int:id>',DeleteCart),
    path('login/',LoginView.as_view() , name='login_url'),
    path('register/',Register,name='register_url'),
    path('logout/',LogOut),
    path('contact/',ContactPage),
    path('sendmess/',Sending),
    path('subtract/<int:id>/',Subtract),
    path('addself/<int:id>/',AddSelf),

   
 ]
 