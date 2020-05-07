#####################################################
# Bot Name : Motarjem Bot                           #
# Version : 1.0                                     #
# Bot Programmer : Iraj Mirzazadeh                  #
# Language : Python3                                #
# Date : Thursday May,7,2020                        #
# This Software is published under GPL3             #
# License is in GPL3.txt with this software         #
#####################################################

# Telegram Library
import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater
from telegram.ext import  CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler

# Other Library
import random
import urllib.request
import json

# pip install googletrans
from googletrans import Translator

# Telegram bot Token
bottok=Telegram Bot Token

# Global flag
c=0

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="به بات مترجم خوش امدید 🤓")

def about(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="🎁 ایرج میرزازاده - ربات تلگرام - پایتون - متن باز 🎁")

def tarjom(update,context):
    global c
    if c==0 or c%2==0:
        context.bot.send_message(chat_id=update.effective_chat.id,text="متن بیگانه 👽 را برای ترجمه به فارسی 🇮🇷 وارد کنید ")
        c=c+1
    matn=update.message.text
    if matn[1:len(matn)] != "tarjom":
        c=c+1
        print(matn)
        translator=Translator(service_urls=['translate.google.com'])
        tarjom=translator.translate(matn,dest='fa')
        context.bot.send_message(chat_id=update.effective_chat.id,text=tarjom.text)

mybot = telegram.Bot(token=bottok)
dictinfo=mybot.get_me()

myupdater = Updater(token=bottok, use_context=True)
mydispatcher = myupdater.dispatcher

mystart_handler = CommandHandler('start', start)
myabout_handler=CommandHandler('about',about)
to_farsi_handler=CommandHandler('tarjom',tarjom)

to_farsi_handler=MessageHandler(Filters.text,tarjom)

mydispatcher.add_handler(mystart_handler)
mydispatcher.add_handler(myabout_handler)
mydispatcher.add_handler(to_farsi_handler)


myupdater.start_polling()
print('working !!!')
