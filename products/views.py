from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from products.forms import AdForm


# Create your views here.
def homepage_view(request):
    return render(request, 'home.html')

def add_product_view(request):
    if request.method == 'POST':
        form= AdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
        else:
            form = AdForm()
    return render(request, 'add_ad.html', {'form': form})
