from typing import Dict
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context: Dict[str, str] = {
        'title': 'Home',
        'content': 'Главная страница магазина - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_authenticated': False
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page')
