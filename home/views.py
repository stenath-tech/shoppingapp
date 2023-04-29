import uuid
import json
import requests
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . models import *
from . forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from userprofile.forms import *
from userprofile.models import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q




# Create your viewspsql here.
def index(request):
    category = Category.objects.all()

    context = {
        'category': category,
    }
    return render(request, 'index.html', context)

def category(request):
    category = Category.objects.order_by('id').all()

    context = {
        'category': category,
    }

    
    return render(request, 'category.html', context)




def product(request):
    product = Product.objects.order_by('id').all()
    context = {
        'product': product,
    }

    return render(request, 'product.html', context)

def categories(request, slug):
    categories = Product.objects.filter(category__slug=slug)
    context = {
        'categories' : categories,
    }
    return render(request, 'categories.html', context)


# def index(request):
#     queryset = Model.objectsManager.get,all,filter,order_by()

#     context ={
#         'queryset': queryset,
#     }
#     return render(request, 'index.html', context)


def details(request, slug):
    details = Product.objects.get(slug=slug)
    context = {
        'details': details,
    }
    return render(request, 'details.html', context)

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your messages was sent successfully")
            return redirect('index')
        else:
            messages.error(request, forms.errors)
            return redirect('index')
    return redirect('index')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('signin')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('signin')


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        pix = request.POST['pix']
        address = request.POST['address']
        dob = request.POST['dob']
        nationality = request.POST['nationality']
        gender = request.POST['gender']
        state = request.POST['state']
        phone = request.POST['phone']
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            newprofile = Profile(user=user)
            newprofile.username = user.username
            newprofile.first_name = user.first_name
            newprofile.last_name = user.last_name
            newprofile.email = user.email
            newprofile.pix = pix
            newprofile.address = address
            newprofile.dob = dob
            newprofile.nationality = nationality
            newprofile.gender = gender
            newprofile.state = state
            newprofile.phone = phone
            newprofile.save()
            login(request, user)
            messages.success(request, "Your account was created" )
            # send_mail(
            #     "Thank You",
            #     "We got your message... and it will be attented to in due time",
            #     settings.EMAIL_HOST_USER
            #     [user.email],
            #     fail_silently=False,
            # )
            return redirect('index')
        else:
            messages.error(request, form.errors)
            return redirect('signup')
    return render(request, 'signup.html')

from django.conf import settings

@login_required(login_url='signin')
def profile(request):
    profile = Profile.objects.get(user__username=request.user.username)
    context = {
        'profile': profile
    }

    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def profile_update(request):
    profile = Profile.objects.get(user__username=request.user.username)
    update = ProfileUpdate(instance=request.user.profile)
    if request.method == 'POST':
        update = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if update.is_valid():
            update.save()
            messages.success(request, 'User profile updated successfully...')
            return redirect('profile')
        else:
            messages.error(request, update.errors)
            return redirect('profileupdate')
    context = {
        'profile': profile,
        'update': update,
    }
    return render(request, 'profile_update.html', context)

@login_required(login_url='signin')
def password(request):
    profile = Profile.objects.get(user__username= request.user.username)
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password change successfully!...')
            return redirect('profile')
        else:
            messages.error(request, forms.errors)
            return redirect('password')
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'password.html',context )

@login_required(login_url='signin')
def shopcart(request):
    if request.method == 'POST':
        quant = int(request.POST['quantity'])
        item_id = request.POST['product_id']
        product = Product.objects.get(pk = item_id)
        order_num = Profile.objects.get(user__username=request.user.username)
        cart_no = order_num.id

        cart = Shopcart.objects.filter(user__username=request.user.username)
        if cart:
            basket = Shopcart.objects.filter(product_id=product.id, user__username=request.user.username, paid=False).first()
            if basket:
                basket.quantity += quant
                basket.amount = product.price * basket.quantity
                basket.save()
                messages.success(request, 'Product added to cart successfully!...')
                return redirect('product')
            else:
                newcart = Shopcart()
                newcart.user = request.user
                newcart.product = product
                newcart.title = product.title
                newcart.price = product.price
                newcart.amount = product.price * quant
                newcart.quantity = quant
                newcart.order_no = cart_no
                newcart.paid = False
                newcart.save()
                messages.success(request, 'Product added in cart successfully!...')
                return redirect('product')
        else:
            newcart = Shopcart()
            newcart.user = request.user
            newcart.product = product
            newcart.title = product.title
            newcart.price = product.price
            newcart.amount = product.price * quant
            newcart.quantity = quant
            newcart.order_no = cart_no
            newcart.paid = False
            newcart.save()
            messages.success(request, 'Product added in cart successfully!...')
            return redirect('product')
    return redirect('product')


@login_required(login_url='signin')
def displaycart(request):
    profile = Profile.objects.filter(user__username=request.user.username)
    trolley = Shopcart.objects.filter(user__username=request.user.username, paid=False)

    subtotal = 0
    vat = 0
    total = 0

    for cart in trolley:
        subtotal += cart.price * cart.quantity
    
    vat = 0.075 * subtotal

    total = subtotal + vat

    context = {
        'profile': profile,
        'trolley': trolley,
        'subtotal': subtotal,
        'vat': vat,
        'total': total,
    }
    return render(request, 'displaycart.html', context)


@login_required(login_url='signin')
def deleteitem(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        deleteitem = Shopcart.objects.get(pk=item_id)
        deleteitem.delete()
        messages.success(request, "Product deleted successfully!...")
    return redirect('displaycart')


@login_required(login_url='signin')
def change(request):
    if request.method == 'POST':
        quant = request.POST['quant']
        product_id = request.POST['product_id']
        modify = Shopcart.objects.get(pk=product_id)
        modify.quantity += quant
        modify.amount = modify.price * modify.quantity
        modify.save()
        messages.success(request, "Cart modified successfully!...")
    return redirect('displaycart')


@login_required(login_url='signin')
def checkout(request):
    profile = Profile.objects.filter(user__username=request.user.username)
    trolley = Shopcart.objects.filter(user__username=request.user.username, paid=False)

    subtotal = 0
    vat = 0
    total = 0

    for cart in trolley:
        subtotal += cart.price * cart.quantity
    
    vat = 0.075 * subtotal

    total = subtotal + vat

    context = {
        'profile': profile,
        'trolley': trolley,
        'total': total,
        'vat': vat,
    }

    return render(request, 'checkout.html', context)


@login_required(login_url='signin')
def pay(request):
    if request.method == 'POST':
        api_key = 'sk_test_1c81d9f5cfe340a94127e9621318ab68640236d4'
        curl = 'https://api.paystack.co/transaction/initialize'
        cburl = 'http://16.16.115.119/callback/'
        ref = str(uuid.uuid4())
        profile = Profile.objects.get(user__username=request.user.username)
        shop_code = profile.id
        total = float(request.POST['total']) * 100
        user = User.objects.get(username=request.user.username)
        first_name = user.first_name
        last_name = user.last_name
        email = user.email
        phone = request.POST['phone']
        address = request.POST['address'] 
        headers = {'Authorization': f'Bearer {api_key}'}
        data = {'reference': ref, 'callback_url': cburl, 'amount': int(total), 'email': user.email, 'order_number': shop_code, 'currency': 'NGN'}

        try:
            r = requests.post(curl, headers=headers, json=data)
        except Exception:
            messages.error(request, "Network busy. Invalid data")
        else:
            transback = json.loads(r.text)
            rdurl = transback['data']['authorization_url']

            account = Payment()
            account.user = user
            account.first_name = user.first_name
            account.last_name = user.last_name
            account.email = user.email
            account.address = address
            account.phone = phone
            account.amount = total/100
            account.pay_code = ref
            account.shop_code = shop_code
            account.paid = True
            account.save()
            return redirect(rdurl)
    return redirect('checkout')

@login_required(login_url='signin')
def callback(request):
    profile = Profile.objects.filter(user__username= request.user.username)
    trolley = Shopcart.objects.filter(user__username= request.user.username, paid=False)
    payment = Payment.objects.filter(user__username= request.user.username, paid=True)


    for items in trolley:
        items.paid = True
        items.save()


        stock = Product.objects.get(pk=items.product_id)
        stock.max_quantity -= items.quantity
        stock.save()

    context ={
        'profile': profile,
        'trolley': trolley,
        'payment': payment,
    }
    return render(request, 'callback.html', context)



def search(request):
    if request.method == 'POST':
        items = request.POST['search']
        searched = Q(Q(title__icontains=items) | Q(description__icontains=items) |Q(category__title__icontains=items) |Q(category__title__icontains=items)  |Q(price__icontains=items))
        searched_items = Product.objects.filter(searched)

        context = {
            'items': items,
            'searched_items': searched_items,
        }
        return render(request, 'search.html', context)
    
    else:
        messages.error
        return render(request, 'search.html', context)