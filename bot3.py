from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
import datetime

from ephem_planets import planet_ephem

planets_list = ["Mars", "Earth", "Moon", "Jupiter", "Neptune", "Sun"]


logging.basicConfig(format="%(name)s -%(levelname)s-%(message)s",
    level=logging.INFO,
    filename="bot.log"
    )

def greet_user(bot, update):
    text = "Вызван /start"
    print(text)

    update.message.reply_text(text)
    #print("Вызван /start")
    #print(update)

def planet_handler(bot, update, args):

    constellation_reply = planet_ephem(args[0])
    print(args)
    update.message.reply_text(constellation_reply)

def wordcounting(bot, update):
    user_text = update.message.text
    if user_text == "/wordcount":
        update.message.reply_text("введите хоть что-нибудь")
    else:
        user_words = len(user_text.split())-1
    if int(repr(user_words)[-1]) ==1:
        update.message.reply_text("введенное значение содержит " + str(user_words) + " слово")
    if 1<int(repr(user_words)[-1])<5:
        update.message.reply_text("введенное значение содержит " + str(user_words) + " слова")
    if int(repr(user_words)[-1])==0:
        update.message.reply_text("введенное значение содержит " + str(user_words) + " слов")
    if int(repr(user_words)[-1])>4:
        update.message.reply_text("введенное значение содержит " + str(user_words) + " слов")
     
def talk_to_me(bot, update):
    user_text=update.message.text
    logging.info(user_text)
    update.message.reply_text(user_text + "?")

def main():
    updater = Updater("460984466:AAE8eUWEA-hLEO3rkQ03xpJRm0StI8Wk_VA")
    dp =updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_handler, pass_args=True)) 
    dp.add_handler(CommandHandler("wordcount", wordcounting))
    dp.add_handler(MessageHandler(Filters.text,talk_to_me))
    updater.start_polling()
    updater.idle()

main()