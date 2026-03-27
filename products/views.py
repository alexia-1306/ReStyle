from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from products.forms import AdForm
from .models import Ad


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
