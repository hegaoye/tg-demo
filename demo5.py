from telegram import Update, ForceReply
from telegram.ext import Application, CallbackContext, MessageHandler, filters

application = Application.builder().token("5512528385:AAFVl3eu7EMoAKIgLyoc3Pmq-wDvRF1vf40").build()


async def echo(update: Update, context: CallbackContext):
    # sending the force reply to the user
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.forcereply.html
    await  update.message.reply_text(reply_markup=ForceReply(selective=True), text="Reply to this message")


application.add_handler(MessageHandler(filters.TEXT, echo))

application.run_polling()
