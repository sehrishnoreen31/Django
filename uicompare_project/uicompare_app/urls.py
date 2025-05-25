from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.compare_images_view, name='compare'),
]
