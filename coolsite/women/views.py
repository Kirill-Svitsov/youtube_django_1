from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.


def index(request):
    return HttpResponse('Страница приложения women.')


def categories(request, slug):
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{slug}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
