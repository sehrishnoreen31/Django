from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blog_id>/', views.details, name='details'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('add_blog/', views.add_new_blog, name='add_blog'),
]
