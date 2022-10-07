import telebot

token = '1682395447:AAGUg3iLK7-edpLWWc-J32fWWnVtH92KBbc'

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
