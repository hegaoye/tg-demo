from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters

application = Application.builder().token("5512528385:AAFVl3eu7EMoAKIgLyoc3Pmq-wDvRF1vf40").build()


async def start(update: Update, context: CallbackContext):
    """
    method to handle the /start command and create keyboard
    """

    # defining the keyboard layout
    kbd_layout = [['大', '小', '单', '双'],
                  ["豹子", "杂三", "顺子"]]

    # converting layout to markup
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardmarkup.html
    kbd = ReplyKeyboardMarkup(kbd_layout)
    username = update.effective_user.username
    await update.message.reply_text(text="@" + username + " 游戏开始", reply_markup=kbd)


async def remove(update: Update, context: CallbackContext):
    """
    method to handle /remove command to remove the keyboard and return back to text reply
    """

    # making a reply markup to remove keyboard
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardremove.html
    reply_markup = ReplyKeyboardRemove()

    # sending the reply so as to remove the keyboard
    await update.message.reply_text(text="暂停游戏", reply_markup=reply_markup)


async def echo(update: Update, context: CallbackContext):
    """
    message to handle any "Option [0-9]" Regrex.
    """
    # sending the reply message with the selected option
    username = update.effective_user.username
    await update.message.reply_text("@" + username + " 点击了 '%s'" % update.message.text)


application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("stop", remove))
application.add_handler(CommandHandler("help", remove))
application.add_handler(MessageHandler(filters.TEXT, callback=echo))

application.run_polling()
