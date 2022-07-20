from telegram import Update, Bot
from telegram.constants import ParseMode
from telegram.ext import CallbackContext, CommandHandler, Application

application = Application.builder().token("5512528385:AAFVl3eu7EMoAKIgLyoc3Pmq-wDvRF1vf40").build()


async def start(update: Update, context: CallbackContext):
    """
    the callback for handling start command
    """
    bot: Bot = context.bot

    # Added HTML Parser to the existing command handler
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.parsemode.html#telegram.ParseMode.HTML
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "Hello User, You have used <b>start</b> command. Search about developer on google, <a href='https://www.google.com/search?q=tbhaxor'>@tbhaxor</a>",
        parse_mode=ParseMode.HTML,
    )
    # bot.send_photo(
    #     chat_id=update.effective_chat.id,
    #     photo=open("/Users/watson/PycharmProjects/tg-bot/img_1.png", 'rb')
    #     # photo=open("/Users/watson/PycharmProjects/tg-bot/img.png", 'rb')
    #
    # )


application.add_handler(CommandHandler("start", start))

application.run_polling()
