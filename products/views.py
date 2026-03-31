from gc import get_objects

from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from products.forms import AdForm
from .models import Ad, Category


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

# def ad_subcategory(request, subcategory):
#     subcategory = SubCategory.objects.get(slug=subcategory)
#     ads = Ad.objects.filter(subcategory=subcategory).order_by('-post_date')
#     return render(request, 'ad_list.html', {'ads': ads, 'subcategory': subcategory})