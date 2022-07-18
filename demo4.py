import sys

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, CallbackQuery
# creating updater
from telegram.ext import Application, CallbackContext, CommandHandler, CallbackQueryHandler

application = Application.builder().token("5512528385:AAFVl3eu7EMoAKIgLyoc3Pmq-wDvRF1vf40").build()


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    sys.stderr.write("ERROR: '%s' caused by '%s'" % context.error, update)


async def start(update: Update, context: CallbackContext):
    """
    callback method handling /start command
    """

    # creating list of input buttons
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinekeyboardbutton.html
    keyboard = [[
        InlineKeyboardButton("充值", callback_data='充值', url="https://www.google.com"),
        InlineKeyboardButton("打折", callback_data='打折',
                             web_app="https://medium.com/@algorithmassasin/build-an-e-commerce-telegram-web-app-bot-f96459e72f79")
    ], [InlineKeyboardButton("小程序", callback_data='小程序')]]

    # creating a reply markup of inline keyboard options
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinekeyboardmarkup.html
    reply_markup = InlineKeyboardMarkup(keyboard)

    # sending the message to the current chat id
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.reply_text
    await update.message.reply_text('Please choose:', reply_markup=reply_markup)


async def button(update, context):
    """
    callback method handling button press
    """
    # getting the callback query
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html
    query: CallbackQuery = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html#telegram.CallbackQuery.answer
    query.answer()

    # editing message sent by the bot
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html#telegram.CallbackQuery.edit_message_text
    await query.edit_message_text(text="您选择了: {}".format(query.data))


# adding listeners
application.add_handler(CommandHandler('start', start))  # handling /start command
application.add_handler(CallbackQueryHandler(button))  # handling inline buttons pressing
application.add_error_handler(error)  # error handling

# started polling
application.run_polling()
