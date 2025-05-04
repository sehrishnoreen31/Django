from django.db import models

# Create your models here.
class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blogs/')
    paragraph = models.TextField(max_length=10000)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    