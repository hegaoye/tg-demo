import re

from telegram import Update
from telegram.ext import Application, CallbackContext, CommandHandler
from telegram.helpers import create_deep_linked_url

application = Application.builder().token("5512528385:AAFVl3eu7EMoAKIgLyoc3Pmq-wDvRF1vf40").build()


async def generate(update: Update, context: CallbackContext):
    """
    method to create a deep link and send it to the current user for sharing
    """

    # generating a sharable link with the payload
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.utils.helpers.html#telegram.utils.helpers.create_deep_linked_url
    url = create_deep_linked_url(context.bot.get_me().username, update.message.chat.username)
    await update.message.reply_text(text="Share it with your friends: %s.\n Copy the link and share it with them" % url)


async def start(update: Update, context: CallbackContext):
    """
    method to run on
    """

    # extracting the payload with /start
    _ = re.findall(r"(?:/start )(.+)", update.message.text)

    # checking if it exists and sending message accordingly
    if len(_) > 0:
        update.message.reply_text(text="You have been refered by: %s" % _[0])
        pass
    else:
        update.message.reply_text(text="Hello, It seems you are new to this bot")
        pass

    await update.message.reply_text(text="Use /generate to create your own referal")


application.add_handler(CommandHandler("generate", generate))
application.add_handler(CommandHandler("start", start))

application.run_polling()
