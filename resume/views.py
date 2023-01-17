from django.shortcuts import render
from django.http import JsonResponse

from .models import Message
from .utils import send_to_telegram


def index(request):
    """ Вывод главной страницы """
    send_to_telegram('Вход')  # Отправка сообщения в Телеграмм-бот
    return render(request, 'index.html', locals())


def save_mess(request):
    """ Функция для получения сообщения из AJAX, вернет ok:1 """
    message = request.POST.get('message')
    Message.objects.create(message=message)
    send_to_telegram(message)  # Отправка сообщения в Телеграмм-бот
    return JsonResponse({'ok': "1"})
