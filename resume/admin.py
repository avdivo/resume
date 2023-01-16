from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):
    """Регистрация таблицы рассылок в админке"""
    list_display = [field.name for field in Message._meta.fields]  # Модель в виде таблицы


admin.site.register(Message, MessageAdmin)  # Регистрируем модель в админке
