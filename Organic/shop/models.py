from django.db import models
from django.utils import timezone

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
    price = models.IntegerField()
    upload_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
