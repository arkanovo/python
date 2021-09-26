import math
import random 
import json

from telegram import InlineQueryResultArticle
from telegram import InputTextMessageContent

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import InlineQueryHandler

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

TOKEN = '2024105989:AAG0GstrehAZ9hAo-NJKdzbeHippLDje66s'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


with open('D:\Code\python\BOT_CONFIG.json', encoding='utf-8') as f:
    BOT_CONFIG = json.load(f)

x = []
y = []

for intent in BOT_CONFIG['intents'].keys():
    try:
        for example in BOT_CONFIG['intents'][intent]['examples']:
            x.append(example)
            y.append(intent)
    except:
        pass

    len(x), len(y), len(set(y))



vectorizer = CountVectorizer()
x_vect = vectorizer.fit_transform(x)

log_reg = LogisticRegression()
log_reg.fit(x_vect, y)

log_reg.score(x_vect, y)

def GetIntentByModel(Text):
    return log_reg.predict(vectorizer.transform([Text]))[0]

GetIntentByModel('Привет')

# функция обработки команды '/start'
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Я КРЕМЛЕБОТ и подчиняюсь только моему господину Аркадию Великому")

# функция обработки текстовых сообщений
def echo(update, context):
    text = 'ECHO: ' + update.message.text 
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)    

# функция обработки не распознных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, 
                             text="Sorry, I didn't understand that command.")

# обработчик команды '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)    

# обработчик текстовых сообщений
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# обработчик не распознных команд
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# запуск прослушивания сообщений
updater.start_polling()
# обработчик нажатия Ctrl+C
updater.idle()