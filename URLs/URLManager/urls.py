from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teams/', views.teams, name='teams'),
    path('teams/<str:name>/', views.team, name='team'),
    path('cities/', views.cities, name='cities'),
]
