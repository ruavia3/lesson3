#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Basic example for a bot that uses inline keyboards.
# This program is dedicated to the public domain under the CC0 license.
"""
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import settings
from ephem_planets import planet_ephem
from currency_converter import USD_converter, EUR_converter

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    keyboard = [[InlineKeyboardButton("Planets", callback_data='Planets'),
                 InlineKeyboardButton("FX Rates", callback_data='FX Rates')],
                [InlineKeyboardButton("Option 3", callback_data='Option 3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Welcome! Please choose:', reply_markup=reply_markup)


def planets(bot, update):
    keyboard = [[InlineKeyboardButton("Mars", callback_data='Mars'),
                 InlineKeyboardButton("Sun", callback_data='Sun')],
                [InlineKeyboardButton("Moon", callback_data='Moon')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    print(update.message)
    if update.message:
        message = update.message
    else:
        message = update.callback_query.message         
    message.reply_text('Please choose:', reply_markup=reply_markup)

def fx_rates(bot, update):
    keyboard = [[InlineKeyboardButton("USD", callback_data='USD'),
                 InlineKeyboardButton("EUR", callback_data='EUR')]]
                
    reply_markup = InlineKeyboardMarkup(keyboard)


    print(update.message)
    if update.message:
        message = update.message
    else:
        message = update.callback_query.message         
    message.reply_text('Please choose:', reply_markup=reply_markup)



def button(bot, update):
    # print('!', update)
    
    query = update.callback_query
    text = query.data
    print('!!', text)

    if text in ['Mars', 'Sun', 'Moon']:
        planet_name = text
        response = planet_ephem(planet_name)

        bot.edit_message_text(text=response,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    elif text == 'Planets':
        planets(bot, update)
    elif text == 'FX Rates':
        fx_rates(bot, update)

    elif text == 'USD':
        ccy2 = 'RUB'
        response = USD_converter(ccy2)
        
        bot.edit_message_text(text=response,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)
    elif text == 'EUR':
        ccy2 = 'RUB'
        response = EUR_converter(ccy2)
        
        bot.edit_message_text(text=response,
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)



def help(bot, update):
    update.message.reply_text("Use /start to test this bot.")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(settings.BOT_TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('planets', planets))
    updater.dispatcher.add_handler(CommandHandler('fx_rates', fx_rates))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
