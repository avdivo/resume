from django.db import models
from django.utils import timezone


class Message(models.Model):
    """Сообщения"""
    message = models.TextField(verbose_name='Сообщение')
    date_create = models.DateTimeField(default=timezone.now, blank=False, verbose_name='Дата создания')
