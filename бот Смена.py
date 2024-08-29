import telebot


import settings

bot = telebot.TeleBot('7094118782:AAHmw3kfJmgTcIsyPnadQB9g5IzhQuPp3tE')
YOUR_CHAT_ID = '5147202190'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет. Напиши любое сообщение и мы опубликуем его в канал', parse_mode='html')

@bot.message_handler()
def get_user_text(message):
    # Пересылаем все полученные сообщения на указанный ID чата
    bot.forward_message(YOUR_CHAT_ID, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Получили твое сообщение. Выложим как можно быстрее :)", parse_mode='html')

bot.polling()

