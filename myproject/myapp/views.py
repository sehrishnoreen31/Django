from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dreamreals
from .forms import DreamRealsForm
# Create your views here.

def home(request):
    return render(request, 'index.html')

def websites(request):
    all_websites = Dreamreals.objects.all()
    return render(request, 'websites.html', {'websites': all_websites})

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

# ---------CRUD OPerations on Dreamreals model---------
# def crud_ops(request):
#     result = ''
#     # add a record
#     if not Dreamreals.objects.filter(name='Polo').exists():
#         dreamreals = Dreamreals(
#             website='polo.com',
#             name = 'Polo',
#             mail = 'polo@co.pk',
#             phonenumber = '03456787560'
#         )
#         dreamreals.save()
#     if not Dreamreals.objects.filter(name='my').exists():
#         dreamreals = Dreamreals(
#             website='my.com',
#             name = 'my',
#             mail = 'my@co.pk',
#             phonenumber = '03456457565'
#         )
#         dreamreals.save()
#     result = 'Added a record in Dreamreals-'

#     # print records
#     records = Dreamreals.objects.all()
#     result += 'Printing the records -'
#     for record in records:
#         result += str(record)+'-'

#     # print one record
#     one_record = Dreamreals.objects.get(website='polo.com')
#     result += 'Print one record-' + str(one_record) + '-'
#     result += one_record.website

#     # deleting a record
#     result += 'Deleting' + one_record.name + '-'
#     one_record.delete()
#     result += 'Deleted Successfully -'


#     # update
#     dreamreals = Dreamreals.objects.get(name='Solex')
#     dreamreals.name = 'UpdatedSolex'
#     dreamreals.save()
#     result += 'Updated' + dreamreals.name + '-'

#     return render(request, 'web.html', {'result': result})
    

def form_add_new(request):
    if request.method == 'POST':
        wb = request.POST['website']
        nm = request.POST['name']
        ml = request.POST['mail']
        pn = request.POST['phone-number']

        # create new object from these details
        new_obj = Dreamreals(website=wb, name=nm, mail=ml, phonenumber=pn)
        new_obj.save()
        return HttpResponse(f'Added a record! {str(new_obj)}')
    return render(request, 'form.html')








