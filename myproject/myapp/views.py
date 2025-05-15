from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def admin(request):
    return render(request, 'admin.html')

def customers(request):
    return render(request, 'customers.html')

def viewArticle(request, articleId):
    text = f'Article Number: {articleId}'
    return HttpResponse(text)

def viewComments(request, commentText):
    text = f'Comment: {commentText}'
    return HttpResponse(text)

def viewSentence(request, sentenceText):
    text = f'Sentence: {sentenceText}'
    return HttpResponse(text)

def viewDate(request, month, year):
    text = f'Date: {month, year}'
    return HttpResponse(text)
    