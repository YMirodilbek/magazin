import email
from multiprocessing import context
from urllib import request
from django.contrib import messages
from http import client
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from.models import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView



def Register(request):
   
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for <strong>{}</strong>'.format(user))
            return redirect('/login/')
    else:
        form = UserCreationForm()
    
    context={
        'form':form
    }
    return render(request, 'registration/register.html',context)

def Login(request):
    product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)
    
    try:
        count =Shop.objects.filter(client=request.user, status=0)[0].item_savatcha.all().count()
    except:
        count = 0
    
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        info = '<strong>{}</strong>. Account was logined !'.format(user)

        messages.success(request,info)


        if user is not None:
            login(request,user)
            redirect('/')
        
        else:
            messages.info(request,'Username or password is incorrect!')
    context={
        'count':count,
        'filteredprod':product1,

    }
    return render(request,'registration/login.html',context)


def LogOut(request):
    r=request.user
    logout(request)
    info = '<strong>{}</strong>. You have successfully loged out!'.format(r)
    messages.success(request,info)
    print(messages)
    return redirect('/login/')

def Home(request):
    try:
        product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)
    except:
        product1 = ShopItems.objects.filter(shop__status = 0)
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
    try:
        count =Shop.objects.filter(client=request.user, status=0)[0].item_savatcha.all().count()
    except:
        count = 0
    context={
        'categ':Category.objects.all(),
        'product':new_product,
        'prod':prod,
        'filteredprod':product1,
        'new-price':new_price,
        'count':count,
    }
    return render(request,'index.html',context)


class ProductDetail(DetailView):
    model = Product
    template_name='product.html'
    context_object_name='product'

    def Prod(request):
        try:
            count =Shop.objects.filter(client=request.user, status=0)[0].item_savatcha.all().count()
        except:
            count = 0
        product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)
        
        context={

            'filteredprod':product1,
            'count':count

        }
        return context

def FilterCateg(request,id):

    return redirect('/')


def new_price(product):
    price = product.price * ((100 - product.discount) / 100)

    return price




@login_required(login_url='login')
def AddToCart(request):
    pr = request.GET.get('product')
    prod = Product.objects.get(id=pr)
    savat = Shop.objects.filter(client=request.user, status=0)
    if len(savat) == 0:
        svt = Shop.objects.create(client=request.user)
    else:
        svt = savat[0]
    new_p = new_price(prod)
    svt.total += new_p
    my_items = ShopItems.objects.filter(shop__client=request.user, shop__status=0, product=prod)
    if len(my_items) == 0:
        ShopItems.objects.create(shop=svt, product=prod, quantity=1, totalPay=new_p)
    else:
        current_item = my_items[0]
        current_item.quantity += 1
        current_item.totalPay += new_p
        current_item.save()

    svt.save()
   
    messages.success(request, f'Savatchaga <strong>{prod.name}</strong> qo`shildi.')
    
    
   
    return redirect('/')

    
def CategoryFilter(request,id):
    print(id)
    product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)

    filter_product = Product.objects.filter(category_id=id)
    try:
        count =Shop.objects.filter(client=request.user, status=0)[0].item_savatcha.all().count()
    except:
        count = 0
    context={
        'categ':Category.objects.all(),
        'filter':filter_product,
        'count':count,
        'filteredprod':product1

    }
    return render(request,'store.html',context)

@login_required(login_url='login_url')
def Cart(request):
    try:
        count =Shop.objects.filter(client=request.user, status=0)[0].item_savatcha.all().count()
    except:
        count = 0
    product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)
    # shopping = Shop.objects.get()
    

    context = {
        'filteredprod':product1,
        # 'order':shop,
        'count':count,
        'shop':Shop.objects.first(),
        
        

        }
    return render(request,'cart.html',context)

# def CheckOut(request):
#     try:
#         count =Shop.objects.filter(client=request.user, status=0)[0].item_savatcha.all().count()
#     except:
#         count = 0
#     product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)
#     shop = Shop.objects.get(status=1)
#     items = ShopItems.objects.filter(shop_id= shop)
#     context = {
#         'filteredprod':product1,
#         # 'order':shop,
#         'count':count,
#         'shop':Shop.objects.first(),
#         'items':items,
#         }
#     return render(request,'checkout.html',context)

# def CheckIt(request):
#     shop = Shop.objects.get(status = 0)
#     shop.status = 1
#     shop.save()
#     return redirect('/checkout/')


# def CountSavatcha(request):
#     count = ShopItems.objects.filter(shop__client=request.user, shop__status=0)
#     s = 0
#     for c in count:
#         s += c.total
#     data = {
#         'count': count.count(),
#         'total': s
#     }

#     return JsonResponse(data)

def DeleteCart(request,id):
    delete = ShopItems.objects.get(id=id)
    shop = Shop.objects.all()
    shop.total -=delete.totalPay
    delete.save()
    delete.delete()

    return redirect('/cart/')



def Blank(request):
    try:
        count =Shop.objects.filter(client=request.user, status=0)[0].item_savatcha.all().count()
    except:
        count = 0
    product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)
    shop=Shop.objects.first()
    context={

        'filteredprod':product1,
        # 'shop':shop,
        'coount':count,
        'categ':Category.objects.all(),


    }
    return render(request,'blank.html',context)


def ContactPage(request):
    try:
        count =Shop.objects.filter(client=request.user, status=0)[0].item_savatcha.all().count()
    except:
        count = 0
    product1 = ShopItems.objects.filter(shop__client = request.user,shop__status = 0)
    
    
    context={
        'count':count,
        'filteredprod':product1
    }
    
    
    return render(request,'contact.html',context)



@login_required(login_url='login_url')
def Sending(request):
    if request.method=='POST':
        r = request.POST
        full_name=r['full_name']
        email=r['email']
        phone=r['phone']
        text=r['text']
        Contact.objects.create(full_name=full_name,email=email,phone=phone,text=text)
        info = '<strong>{}</strong>. Xabaringiz Yuborildi! , Tez orada aloqaga chiqamiz'.format(full_name)
        messages.success(request,info)

    return redirect('/contact/')

def Subtract(request):

    shop = ShopItems.objects.get()
    shop.quantity -= 1
    shop1=Shop.objects.get()

    # if shop.product.discount:
    #     shop.totalPay -= shop.product.discount
    # else:
    shop1.total -= shop.product.price 
    shop.totalPay -= shop.product.price

    shop1.save()
    shop.save()
    return redirect('/cart/')

 
def AddSelf(request):
    
    shop = ShopItems.objects.get()
    shop.quantity += 1
    shop1=Shop.objects.get()
    # if shop.product.discount:
    #     shop.totalPay += shop.product.discount
    # else:
    shop1.total += shop.product.price
    shop.totalPay += shop.product.price
    shop.save()
    shop1.save()
    return redirect('/cart/')


    

