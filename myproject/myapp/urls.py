from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('admin/', views.admin, name='admin'),
    path('customers/', views.customers, name='customers'),
    # path('webs/', views.crud_ops, name='webs'),
    path('form/', views.form_add_new, name='form_add_new'),
    # path('djangoforms/', views.form_add_new_djangoForms, name='form_add_new_djangoForms'),
    re_path(r'^viewArticle/(\d+)/', views.viewArticle, name='viewArticle'), #int
    re_path(r'^viewComments/([\w-]+)/', views.viewComments, name='viewComments'), #string
    re_path(r'^viewSentence/(.+)/', views.viewSentence, name='viewSentence'), #sentence
    re_path(r'^viewDate/(\d{2})/(\d{4})/', views.viewDate, name='viewDate'), #date
]


