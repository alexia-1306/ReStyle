from django.urls import path, include
from products import views
from products.views import add_product_view

urlpatterns = [
    path("users/", include("users.urls")),
    path("/add-ad/", add_product_view, name="add_ad"),
]
