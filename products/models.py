from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    parent_category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)

    def subcategories(self):
        return Category.objects.filter(parent_category=self)
    def __str__(self):
        return f'{self.name}'



class Ad(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    city = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    post_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=255, choices=(
        ('open', 'Deschis'),
        ('closed', 'Inchis'),
        ('paid', 'Platit'),
        ('retour', 'Retur'),
    ))

    # def cart_items(self):
    #     return CartItem.objects.filter(cart=self)

    def total(self):
        total = 0
        for item in CartItem.objects.filter(cart=self):
            total += item.total()
        return total

    def __str__(self):
        return f'{self.status} cart belongs to {self.user}'

class CartItem(models.Model):
    product = models.ForeignKey(Ad, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def total(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'{self.quantity} X {self.product} in cart {self.cart}'
