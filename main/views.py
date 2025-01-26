from typing import Dict
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    context: Dict[str, str] = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME'
    }

    return render(request, 'main/index.html', context)


def about(request):
    context: Dict[str, str] = {
        'title': 'Home - О нас',
        'content': 'О НАС',
        'text_on_page': "Текст о том какой магазин класный с таким хорошим товаром" 
    }

    return render(request, 'main/about.html', context)
