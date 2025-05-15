from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Home Page')

def teams(request):
    all_teams = {
        'pak': ['Babar', 'Rizwan', 'Amir', 'Shaheen',],
        'ind': ['Kohli', 'Rohit', 'Shubman', 'Pandya'],
        'nz': ['Kane', 'Danial', 'McCullum', 'Santner'],
        'eng': ['Morgan', 'Joe', 'Willy']
    }
    return render(request, 'teams.html', {'all_teams': all_teams.keys()})

def team(request, name):
    teams_data = {
        'pak': ['Babar', 'Rizwan', 'Amir', 'Shaheen',],
        'ind': ['Kohli', 'Rohit', 'Shubman', 'Pandya'],
        'nz': ['Kane', 'Danial', 'McCullum', 'Santner'],
        'eng': ['Morgan', 'Joe', 'Willy']
    }
    team = teams_data.get(name.lower(), 'Not Found')
    return render(request, 'team.html', {'team': team, 'name':name})

def cities(request):
    all_cities = ['Lahore', 'Islamabad', 'Karachi']
    return render(request, 'cities.html', {'all_cities': all_cities})