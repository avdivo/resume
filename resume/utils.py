import telebot
from django.conf import settings

def send_to_telegram(text):
    token = settings.TBOT_TOKEN
    bot = telebot.TeleBot(token)
    chat_id = settings.CHAT_ID
    bot.send_message(chat_id, 'AVDIVO: ' + text)