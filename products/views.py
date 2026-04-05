from gc import get_objects

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from products.forms import AdForm
from .models import Ad, Category, Favorites, Cart, CartItem, Order


# Create your views here.
def homepage_view(request):
    return render(request, 'home.html')

def add_product(request):
    if request.method == 'POST':
        form= AdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdForm()
    return render(request, 'add_product.html', {'form': form})

def ad_list(request):
    ads = Ad.objects.all().order_by('-post_date')
    return render(request, 'ad_list.html', {'ads': ads})

def ad_category(request, category):
    category = Category.objects.get(slug=category)
    ads = Ad.objects.filter(category=category).order_by('-post_date')
    return render(request, 'ad_list.html', {'ads': ads, 'category': category})

def ad_detail(request, ad_id):
    ad_details = Ad.objects.get(id=ad_id)

    return render(request, 'ad_detail.html', {'ad_details': ad_details})

@login_required(login_url='login')
def favorites(request, ad_id):
    fav, create = Favorites.objects.get_or_create(user=request.user, ad=Ad.objects.get(id=ad_id))
    if create:
        pass
    else:
        fav.delete()
    return redirect('ad_list')

def fav_list(request):
    favs = Favorites.objects.filter(user=request.user)
    return render(request, 'favorites_list.html', {'favs': favs})
@login_required(login_url='login')
def add_to_cart(request, ad_id):
    cart, created = Cart.objects.get_or_create(status='open', user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=Ad.objects.get(id=ad_id))
    cart_item.quantity += 1
    cart_item.save()
    return redirect('ad_list')


def remove_from_cart(request, ad_id):
    cart = Cart.objects.get(user=request.user, status='open')
    cart_item = CartItem.objects.get(cart=cart, product=Ad.objects.get(id=ad_id))
    cart_item.delete()

    return redirect('cart_detail')

def cart_detail(request):
    cart_details, created = Cart.objects.get_or_create(user=request.user, status='open')
    items = CartItem.objects.filter(cart=cart_details)
    return render(request, 'cart.html', {'cart_details': cart_details, 'items': items})


def checkout(request):
    cart_details = Cart.objects.get(user=request.user, status='open')
    if request.method == 'POST':
        Order.objects.create(user=request.user, cart=cart_details, adress=request.POST.get('adress'))
        cart_details.status = 'closed'
        cart_details.save()
        return redirect('cart_detail')

    return render(request, 'checkout.html', {'cart_details': cart_details})
