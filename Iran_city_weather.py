#####################################################
# Bot Name Iran Tool Bot                            #
# Version : 1.0                                     #
# Bot Programmer : Iraj Mirzazadeh                  #
# Language : Python3                                #
# Date : Friday May,1,2020                          #
# This Software is published under GPL3             #
# License is in GPL3.txt with this software         #
#####################################################

# Main Telegram Bot Classes
import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater
from telegram.ext import  CallbackQueryHandler
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import InlineQueryHandler

# Extra Classes and Modules
import random
import urllib.request
import json


#tokens
bottok='1285793973:AAErnAypLeY6H1nR6tR0emwis05ByVvnBOo'
wtok='90d43f5cd589307cc368e317b6d4d198'

#commands
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="به ربات جعبه ابزار خوش آمدید 😊")
    print("start")
def about(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="🎁 ایرج میرزازاده - ربات تلگرام - پایتون - متن باز 🎁")
    print("about")
def weather(update, context):
    mykeyboard = [[InlineKeyboardButton("تهران", callback_data='Tehran'),InlineKeyboardButton("مشهد", callback_data='Mashhad'),InlineKeyboardButton("اصفهان", callback_data='Isfahan'),InlineKeyboardButton("تبریز", callback_data='Tabriz'),InlineKeyboardButton("کرج", callback_data='Karaj'),InlineKeyboardButton("شیراز", callback_data='Shiraz')],
                  [InlineKeyboardButton("قم", callback_data='Qom'),InlineKeyboardButton("اهواز", callback_data='Ahvaz'),InlineKeyboardButton("ارومیه", callback_data='Urmia'),InlineKeyboardButton("رشت", callback_data='Rasht'),InlineKeyboardButton("زاهدان", callback_data='Zahedan')],
                  [InlineKeyboardButton("همدان", callback_data='Hamadan'),InlineKeyboardButton("کرمان", callback_data='Kerman'),InlineKeyboardButton("یزد", callback_data='Yazd'),InlineKeyboardButton("اردبیل", callback_data='Ardabil'),InlineKeyboardButton("اراک", callback_data='Arak')],
                  [InlineKeyboardButton("قزوین", callback_data='Qazvin'),InlineKeyboardButton("زنجان", callback_data='Zanjan'),InlineKeyboardButton("خرم آباد", callback_data='Khorramabad'),InlineKeyboardButton("سنندج", callback_data='Sanandaj'),InlineKeyboardButton("گرگان", callback_data='Gorgan'),InlineKeyboardButton("ساری", callback_data='Sari')],
                  [InlineKeyboardButton("بجنورد", callback_data='Bojnord'),InlineKeyboardButton("بوشهر", callback_data='Bushehr'),InlineKeyboardButton("بیرجند", callback_data='Birjand'),InlineKeyboardButton("ایلام", callback_data='Ilam'),InlineKeyboardButton("سمنان", callback_data='Semnan')],
                  [InlineKeyboardButton("یاسوج", callback_data='Yasuj'),InlineKeyboardButton("کرمانشاه", callback_data='Kermanshah'),InlineKeyboardButton("بندر عباس", callback_data='Bandar Abbas'),InlineKeyboardButton("شهرکرد", callback_data='Shahre Kord')]]
    reply_markup = InlineKeyboardMarkup(mykeyboard)
    update.message.reply_text('شهر مورد نظر را جهت مشاهده اب و هوا انتخاب کنید 😄', reply_markup=reply_markup)
def button(update,context):
    query = update.callback_query
    query.answer()
    url=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+str(query.data)+'&appid='+str(wtok))
    dict=json.loads(url.read())
    city="City : "+str(dict['name'])
    print(dict['name'])
    context.bot.send_message(chat_id=update.effective_chat.id,text=city)
    degree=int(dict['main']['temp'])-273
    if degree<0:
        condition="Degree : "+str(degree)+" Celcius ☃️"
    elif degree==0:
        condition="Degree : "+str(degree)+" Celcius ❄️"
    else:
        condition="Degree : "+str(degree)+" Celcius 🌞"
    context.bot.send_message(chat_id=update.effective_chat.id,text=condition)
    w=dict['weather'][0]['main']
    if w=='Clear sky' or w=='Clear':
        weather=str(dict['weather'][0]['main'])+","+str(dict['weather'][0]['description'])+" ☀️"
    elif w=='few clouds' or w=='scattered clouds' or w=='broken clouds':
        weather=str(dict['weather'][0]['main'])+","+str(dict['weather'][0]['description'])+" ⛅️"
    elif w=='shower rain' or w=='Rain':
        weather=str(dict['weather'][0]['main'])+","+str(dict['weather'][0]['description'])+" ⛈"
    elif w=='Clouds':
        weather=str(dict['weather'][0]['main'])+","+str(dict['weather'][0]['description'])+" ☁️"
    elif w=='Thunderstorm' or 'Tornado':
        weather=str(dict['weather'][0]['main'])+","+str(dict['weather'][0]['description'])+" 🌩🌪"
    elif w=='Snow':
        weather=str(dict['weather'][0]['main'])+","+str(dict['weather'][0]['description'])+" 🌨❄️"
    elif w=='Mist' or w=='Smoke' or w=='Fog' or w=='Haze' or w=='Dust' or w=='Squall' :
        weather=str(dict['weather'][0]['main'])+","+str(dict['weather'][0]['description'])+" 🌫🌫"
    elif w=='Drizzle':
        weather=str(dict['weather'][0]['main'])+","+str(dict['weather'][0]['description'])+" 🌦"
    elif w=='Ash':
        weather=str(dict['weather'][0]['main'])+","+str(dict['weather'][0]['description'])+" 🌫🌋"
    else:
        weather=str(dict['weather'][0]['main'])+","+str(dict['weather'][0]['description'])
    context.bot.send_message(chat_id=update.effective_chat.id,text=weather)


# Main codes
# Bot object creation
mybot = telegram.Bot(token=bottok)
dictinfo=mybot.get_me()

# Create Updater & dispatcher
myupdater = Updater(token=bottok, use_context=True)
mydispatcher = myupdater.dispatcher

# commands
mystart_handler=CommandHandler('start',start)
myabout_handler=CommandHandler('about',about)
myweather_handler=CommandHandler('weather',weather)


# dispatcher
mydispatcher.add_handler(CallbackQueryHandler(button))
mydispatcher.add_handler(myweather_handler)
mydispatcher.add_handler(mystart_handler)
mydispatcher.add_handler(myabout_handler)



# Bot starts
myupdater.start_polling()
print('working !!!')
