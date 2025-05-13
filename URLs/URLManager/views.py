from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home Page')

def teams(request, name):
    teams_data = {
        'pak': ['Babar', 'Rizwan', 'Amir', 'Shaheen',],
        'ind': ['Kohli', 'Rohit', 'Shubman', 'Pandya'],
        'nz': ['Kane', 'Danial', 'McCullum', 'Santner'],
        'eng': ['Morgan', 'Joe', 'Willy']
    }
    team = teams_data.get(name.lower(), 'Not Found')
    return render(request, 'index.html', {'team': team, 'name':name})

