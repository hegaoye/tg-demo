from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Application

application = Application.builder().token("5512528385:AAFVl3eu7EMoAKIgLyoc3Pmq-wDvRF1vf40").build()


async def generate(update: Update, context: CallbackContext):
    # initializing the bot with API
    info = context.bot.bot
    print(info)


application.add_handler(CommandHandler("start", generate))
application.run_polling()
