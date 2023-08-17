from django.shortcuts import render
from django.http import JsonResponse

from .models import Message
from .utils import send_to_telegram
from user_agents import parse


def index(request):
    """ Вывод главной страницы """

    user_agent = parse(request.META['HTTP_USER_AGENT'])

    if not user_agent.is_bot:
        msg = f'Вход с {user_agent.device.family} {user_agent.browser.family} {user_agent.os.family}'
    else:
        msg = f'Вход Бота'
    send_to_telegram(msg)

    return render(request, 'index.html', locals())


def save_mess(request):
    """ Функция для получения сообщения из AJAX, вернет ok:1 """
    message = request.POST.get('message')
    Message.objects.create(message=message)
    send_to_telegram(message)  # Отправка сообщения в Телеграмм-бот
    return JsonResponse({'ok': "1"})
