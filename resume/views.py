from django.shortcuts import render
from django.http import JsonResponse

from .models import Message


def index(request):
    """ Вывод главной страницы """
    return render(request, 'index.html', locals())


def save_mess(request):
    """ Функция для получения сообщения из AJAX, вернет ok:1 """
    Message.objects.create(message=request.POST.get('message'))
    return JsonResponse({'ok': "1"})
