import types

import telebot
import random

from telebot import types

bot = telebot.TeleBot("5889288089:AAGmNcTf9-z-J9_xCewPFL59xEvC8FxWfLk")

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('sticker.webp','rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("КАК ДЕЛА")
    item2 = types.KeyboardButton("ЧТО ДЕЛАЕШЬ")
    item3 = types.KeyboardButton("КАКИЕ ПЛАНЫ")
    item4 = types.KeyboardButton("ЧЕМ ЗАНЯТ")
    item5 = types.KeyboardButton("СКОЛЬКО ТЕБЕ ЛЕТ")
    item6 = types.KeyboardButton("КАК ТЕБЯ ЗОВУТ")
    item7 = types.KeyboardButton("КАКИЕ ТВОИ ЛЮБИМЫЕ ИГРЫ")
    item8 = types.KeyboardButton("ГДЕ ТЫ ЖИВЁШЬ")
    item9 = types.KeyboardButton("КАКОЙ ТВОЙ ЛЮБИМЫЙ ЦВЕТ")
    item10 = types.KeyboardButton("КАКОЕ ТВОЁ ЛЮБИМОЕ ЖИВОТНОЕ")
    markup.add(item1,item2,item3,item4,item5,item6,item7,item8,item9,item10)
    bot.send_message(message.chat.id, f"ПРИВЕТ,{message.from_user.first_name}!".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['kek'])
def welcome(message):
    bot.send_message(message.chat.id, "что станет с вороной если она сядит на провода ----- электрокар")
@bot.message_handler(commands=['vafle'])
def send_welcome(message):
    stiq = open('dfakz.jpg','rb')
    bot.send_sticker(message.chat.id, stiq)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Значит у нас есть команда /kek это шутка и /vafle это картинка')

@bot.message_handler(commands=['shum'])
def send_welcome(message):
    stiq = open('les-zvuki-lesa.mp3','rb')
    bot.send_sticker(message.chat.id, stiq)

@bot.message_handler(content_types=('text'))
def lalala(message):
    if message.text.lower()=="что делаешь":
        bot.send_message(message.chat.id, 'ДЕЛАЮ ДЗ А ТЫ')

    if message.text.lower() == "как дела":
        bot.send_message(message.chat.id, 'Да всё хорошо')

    if message.text.lower() == "какие планы":
        bot.send_message(message.chat.id, 'Пойду погуляю')
    if message.text.lower() == "чем занят":
        bot.send_message(message.chat.id, 'С тобой переписываюсь')
    if message.text.lower() == "сколько тебе лет":
        bot.send_message(message.chat.id, 'много')
    if message.text.lower() == "как тебя зовут":
        bot.send_message(message.chat.id, 'fixoreggbot')
    if message.text.lower() == "какие твои любимые игры":
        bot.send_message(message.chat.id, 'FarCry3, hoi4, Factorio, my summer car')
    if message.text.lower() == "где ты живёшь":
        bot.send_message(message.chat.id, 'в телеграме')
    if message.text.lower() == "какой твой любимый цвет":
        bot.send_message(message.chat.id, 'синий')
    if message.text.lower() == "какое твоё любимое животное":
        bot.send_message(message.chat.id, 'бобр')
    else:
        bot.send_message(message.chat.id, 'ДА ТЫ ОДУРЕЛ Я НЕ ЗНАЮ')

bot.polling()

