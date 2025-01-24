from time import process_time

import telebot

user_data = {}

TOKEN = "8190098817:AAF6jqh-AM4QHUbUBjg_vZExAXc8Swyyt20"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Ну привет я помогу узнать тебе сколько ты сможешь купить робуксов")
    bot.send_message(message.chat.id, "Вот список команд:")
    bot.send_message(message.chat.id, "/hi - бот тебя поприветствует")
    bot.send_message(message.chat.id, "/ind - перевод денег в робуксы")

@bot.message_handler(commands=["hi"])
def hi(message):
    bot.reply_to(message, "ну привет")

@bot.message_handler(commands=["ind"])
def ind(message):
    bot.reply_to(message, "Введи количество денег, которое у тебя есть")
    bot.register_next_step_handler(message, process_money_input)

def process_money_input(message):
    try:
        money = float(message.text)
        robux = money / 0.75
        bot.reply_to(message, f"{round(robux)} робуксов")
    except ValueError:
        bot.reply_to(message, "введи нормальное число")


bot.polling(none_stop=True)
