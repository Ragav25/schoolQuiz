import requests
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    url = 'https://opentdb.com/api.php?amount=10&category={}&type=multiple'
    category = 19

    r = requests.get(url.format(category)).json()
    print(r['results'][0]['question'])
    return render(request, 'home.html', {'name': 'John'})
