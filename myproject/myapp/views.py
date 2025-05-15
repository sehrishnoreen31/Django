from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = 'This a django app'
    return HttpResponse(text)

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
