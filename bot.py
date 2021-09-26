import math
import random 
import nltk
import json

from telegram import InlineQueryResultArticle
from telegram import InputTextMessageContent
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import InlineQueryHandler

TOKEN = '2024105989:AAG0GstrehAZ9hAo-NJKdzbeHippLDje66s'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

with open('/BOT_CONFIG.json', 'r') as f:
    BOT_CONFIG = json.load(f)


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