from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

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



    def __str__(self):
        return f'{self.name}'

