from django.urls import path, include
from products import views
from products.views import add_product
urlpatterns = [
    path("add-ad/", add_product, name="add_ad"),
    path("ads/", views.ad_list, name="ad_list"),
    path('ads/category/<slug:category>/', views.ad_category, name="ad_category"),
    path('favorites/<int:ad_id>', views.favorites, name="favorites"),
    path('favorites/',views.fav_list, name="fav_list" ),
    ]
