from django.urls import path, include
from products import views
from products.views import add_product
urlpatterns = [
    path("add-ad/", add_product, name="add_ad"),
    path("ads/", views.ad_list, name="ad_list"),
    path('ads/category/<slug:category>/', views.ad_category, name="ad_category"),
    path('favorites/<int:ad_id>', views.favorites, name="favorites"),
    path('favorites/',views.fav_list, name="fav_list" ),
    path('ad/<int:ad_id>/',views.ad_detail, name="ad_detail"),
    path('cart/', views.cart_detail, name="cart_detail"),
    path('cart/add/<int:ad_id>/', views.add_to_cart, name="add_to_cart"),
    path('cart/remove/<int:ad_id>/', views.remove_from_cart, name="remove_from_cart"),
    path('cart/checkout/', views.checkout, name="checkout"),
    path('search/', views.search, name="search"),
    path('messages/<int:ad_id>/', views.send_message, name="send_message"),
    path('inbox/', views.inbox, name="inbox"),
    ]
