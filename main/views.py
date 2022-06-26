from django.contrib import messages
from http import client
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from.models import *
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

def Login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        log = authenticate(request,username=username,password=password)
        print(username,password)
        if log is not None:
            login(request,log)
            messages.success(request,'Tizimga Kirildi!')
            return redirect('/')
        else:
            messages.error(request,'login yoki userrname xato!')
            return redirect('/login/')        

    return render(request,'login.html')

def Register(request):
    if request.method=='POST':
        l = request.POST
        username = l['username']
        password = l['password']
        first_name = l['first_name']
        last_name = l['last_name']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return redirect('/login/')
        else:
            user=User.objects.create(username=username, password=password, first_name=first_name, last_name=last_name)
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
            return redirect('/')

    else:
        return render(request, 'register.html')



    

