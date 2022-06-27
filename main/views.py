import email
from django.contrib import messages
from http import client
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from.models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
# Create your views here.

@login_required
def Home(request):
    product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)
    product = Product.objects.all()
    prod = Product.objects.filter(Is_New=True)

    new_product=[]
    for i in product:
        
        if i.discount > 0:
            new_price = i.price * ((100-i.discount)/100)
            item = {
                'id':i.id,
                'category':i.category,
                'name':i.name,
                'photo':i.photo,
                'price':i.price,
                'discount':new_price,
               
            }
        else:
            item={
                'id':i.id,  
                'category':i.category,
                'name':i.name,
                'photo':i.photo,
                'price':i.price,
                

            }
        new_product.append(item)
    context={
        'categ':Category.objects.all(),
        'product':new_product,
        'prod':prod,
        'filteredprod':product1,
        'new-price':new_price,
    }
    return render(request,'index.html',context)


class ProductDetail(DetailView):
    model = Product
    template_name='product.html'
    context_object_name='product'


def FilterCateg(request,id):

    return redirect('/')


def AddToCart(request,id):
    user = request.user
    shop = Shop.objects.filter(client=user , status = 0)
    if len(shop)==0:
        shop=Shop.objects.create(client=user)
    else:
   
        shop=Shop.objects.get( client=user , status = 0)

    product = Product.objects.get(id=id)

    if product.discount:
        ShopItems.objects.create(shop=shop,product=product,quantity=1,total=product.discount)
        shop.total +=product.discount
        shop.save()
    else:
        ShopItems.objects.create(shop=shop,product=product,quantity=1,total=product.price)
        shop.total +=product.price
        shop.save()
    

    return redirect('/')

def CategoryFilter(request,id):
    print(id)
    filter_product = Product.objects.filter(category_id=id)
    context={
        'categ':Category.objects.all(),
        'filter':filter_product

    }
    return render(request,'store.html',context)

def Cart(request):
    product = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)

    context ={
        'filteredprod':product
    }
    return render(request,'cart.html',context)

def CountSavatcha(request):
    count = ShopItems.objects.filter(shop__client=request.user, shop__status=0)
    s = 0
    for c in count:
        s += c.total
    data = {
        'count': count.count(),
        'total': s
    }

    return JsonResponse(data)

def DeleteCart(request,id):
    delete = ShopItems.objects.get(id=id)
    delete.delete()

    return redirect('/cart/')


def Register(request):
    form = UserCreationForm() 
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print(f'form.email')
    context = {
        'form':form,
    } 
    
    return render(request,'register.html',context)

def Login(request):
    return render(request,'login.html')
 

def ContactPage(request):
 
    return render(request,'contact.html')

def Sending(request):
    if request.method=='POST':
        r = request.POST
        full_name=r['full_name']
        email=r['email']
        phone=r['phone']
        text=r['text']
        Contact.objects.create(full_name=full_name,email=email,phone=phone,text=text)
       
    return redirect('/contact/')



    

