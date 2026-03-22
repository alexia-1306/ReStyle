from django.urls import path, include
from products import views
from products.views import add_product
urlpatterns = [
    path("add-ad/", add_product, name="add_ad"),
]
