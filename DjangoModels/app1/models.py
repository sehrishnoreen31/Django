from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    USER_TYPE = [
        ('AD', 'ADMIN'),
        ('BY', 'BUYER'),
        ('SE', 'SELLER'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='users/')
    data_added = models.DateField(default=timezone.now)
    user_type = models.CharField(max_length=2, choices=USER_TYPE)

    def __str__(self):
        return self.name
