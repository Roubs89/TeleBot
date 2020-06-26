import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def welcome(message):
    bot.send_message(message.chat.id, message.text)

# RUN11
bot.polling(none_stop=True)
