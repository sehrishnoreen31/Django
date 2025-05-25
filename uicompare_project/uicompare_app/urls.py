from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('compare/', views.compare_images_view, name='compare'),
]
