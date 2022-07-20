import sys

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, CallbackQuery, CallbackGame
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
    demo_url = "https://www.wangcai321.com/bot/web/player.html?g=-1001756231525&t=YAyEYzQlNZ2w2Fo1658210341868#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DVQfENQsIeEniRnaKwcQE"
    g = CallbackGame()
    g.set_bot(context.bot)
    keyboard = [
        [
            InlineKeyboardButton(text="小程序", callback_game=g)
            # InlineKeyboardButton(text="小程序", web_app=WebAppInfo(url=demo_url))
            # InlineKeyboardButton(text="小程序", web_app=WebAppInfo(url="https://webapp.1akzl9mvs.com/"))
            # InlineKeyboardButton(text="小程序", web_app=WebAppInfo(url="https://python-telegram-bot.org/static/webappbot"))
        ]

    ]

    # creating a reply markup of inline keyboard options
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.inlinekeyboardmarkup.html
    reply_markup = InlineKeyboardMarkup(keyboard)
    # sending the message to the current chat id
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.message.html#telegram.Message.reply_text
    # await update.message.reply_game(game_short_name="thisiswatsonsdemogame")
    await update.message.reply_game(game_short_name="thisiswatsonsdemogame", reply_markup=reply_markup)
    # await update.message.reply_text('Please choose:', reply_markup=reply_markup)


async def button(update, context: CallbackContext):
    """
    callback method handling button press
    """
    # getting the callback query
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html
    query: CallbackQuery = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html#telegram.CallbackQuery.answer
    demo_url = "https://www.wangcai321.com/bot/web/player.html?g=-1001756231525&t=YAyEYzQlNZ2w2Fo1658210341868#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DVQfENQsIeEniRnaKwcQE"

    await query.answer(text="open", url=demo_url)
    # editing message sent by the bot
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html#telegram.CallbackQuery.edit_message_text
    # await query.edit_message_text(text="您选择了: {}".format("小程序"))


# adding listeners
application.add_handler(CommandHandler('start', start))  # handling /start command
application.add_handler(CallbackQueryHandler(button))  # handling inline buttons pressing
application.add_error_handler(error)  # error handling

# started polling
application.run_polling()
