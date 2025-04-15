from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# home page 
def home(request):
    text = 'This is a demo app!'
    return HttpResponse(text)