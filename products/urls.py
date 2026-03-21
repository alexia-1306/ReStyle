from django.urls import path, include
from products import views


urlpatterns = [
    path("users/", include("users.urls")),
]
