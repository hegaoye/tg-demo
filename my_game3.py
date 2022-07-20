from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup, CallbackQuery
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters, CallbackQueryHandler

application = Application.builder().token("5241392506:AAFm2rwARsgBOmmf9Zw9vVfqANcs3-cdBr8").build()


async def start(update: Update, context: CallbackContext):
    """
    method to handle the /start command and create keyboard
    """

    # defining the keyboard layout
    kbd_layout = [
        ['大 50', '小 50', '单 50', '双 50'],
        ['查看投注', '小程序', '帮助']
    ]

    kbd = ReplyKeyboardMarkup(keyboard=kbd_layout, resize_keyboard=True)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="欢迎使用星彩娱乐",
        reply_markup=kbd
    )


async def remove(update: Update, context: CallbackContext):
    """
    method to handle /remove command to remove the keyboard and return back to text reply
    """

    # making a reply markup to remove keyboard
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardremove.html
    reply_markup = ReplyKeyboardRemove()

    # sending the reply so as to remove the keyboard
    await update.message.reply_text(text="暂停游戏", reply_markup=reply_markup)


async def send_game_message(update: Update, context: CallbackContext):
    """
    the callback for handling start command
    """
    issue = """
    第20220720888期合计投注:
    大:{big}
    小:{small}
    单:{even}
    双:{odd}
    号码:{num}
    {at}
    """
    click_button_text = update.message.text
    if click_button_text.__contains__('小程序'):
        await context.bot.send_game(
            chat_id=update.effective_chat.id,
            game_short_name="zijietiaodonggame"
        )
    elif click_button_text.__contains__('大'):
        username = update.effective_user.username
        text = issue.format(at="@" + username, big=update.message.text, small="0", even="0", odd="0", num="无")
        await update.message.reply_text(text)
    elif click_button_text.__contains__('小'):
        username = update.effective_user.username
        text = issue.format(at="@" + username, big="0", small=update.message.text, even="0", odd="0", num="无")
        await update.message.reply_text(text)
    elif click_button_text.__contains__('单'):
        username = update.effective_user.username
        text = issue.format(at="@" + username, big="0", small="0", even=update.message.text, odd="0", num="无")
        await update.message.reply_text(text)
    elif click_button_text.__contains__('双'):
        username = update.effective_user.username
        text = issue.format(at="@" + username, big="0", small="0", even="0", odd=update.message.text, num="无")
        await update.message.reply_text(text)
    elif click_button_text.__contains__('投注'):
        username = update.effective_user.username
        await update.message.reply_text("@" + username + " 点击了 '%s'" % update.message.text + "，查询投注中，请稍等")
    elif click_button_text.__contains__('帮助'):
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("/Users/watson/PycharmProjects/tg-bot/img_1.png", 'rb')
        )


async def button(update, context: CallbackContext):
    """
    callback method handling button press
    """
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html
    query: CallbackQuery = update.callback_query

    demo_url = "https://www.wangcai321.com/bot/web/player.html?g=-1001756231525&t=YAyEYzQlNZ2w2Fo1658210341868#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DVQfENQsIeEniRnaKwcQE"
    await query.answer(text="open", url=demo_url)


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

application.add_handler(CallbackQueryHandler(button))
application.add_handler(MessageHandler(filters.TEXT, callback=send_game_message))
# application.add_handler(MessageHandler(filters.TEXT, callback=echo))

application.run_polling()
