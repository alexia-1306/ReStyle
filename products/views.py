from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
def homepage_view(request):
    return render(request, 'home.html')