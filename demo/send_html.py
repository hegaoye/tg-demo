from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup, CallbackGame
from telegram.constants import ParseMode
from telegram.ext import CallbackContext, CommandHandler, Application

application = Application.builder().token("5512528385:AAFVl3eu7EMoAKIgLyoc3Pmq-wDvRF1vf40").arbitrary_callback_data(
    True).build()


async def start(update: Update, context: CallbackContext):
    """
    the callback for handling start command
    """
    bot: Bot = context.bot

    demo_url = "https://www.google.com"
    # demo_url = "tg://www.wangcai321.com/bot/web/player.html?g=-1001756231525&t=YAyEYzQlNZ2w2Fo1658210341868#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DVQfENQsIeEniRnaKwcQE"
    keyboard = [
        [
            InlineKeyboardButton(text="小程序", url=demo_url, callback_game=CallbackGame("thisiswatsonsdemogame"))
            # InlineKeyboardButton(text="小程序", web_app=WebAppInfo(url="https://webapp.1akzl9mvs.com/"))
            # InlineKeyboardButton(text="小程序", web_app=WebAppInfo(url="https://webapp.1akzl9mvs.com/"))
            # InlineKeyboardButton(text="小程序", web_app=WebAppInfo(url="https://python-telegram-bot.org/static/webappbot"))
        ]

    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Added HTML Parser to the existing command handler
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.parsemode.html#telegram.ParseMode.HTML
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=
        "Hello User, You have used <b>start</b> command. Search about developer on google, <a href='https://www.google.com/search?q=tbhaxor' target='_self'>@tbhaxor</a>",
        parse_mode=ParseMode.HTML,
        reply_markup=reply_markup
    )

    await bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open("/Users/watson/PycharmProjects/tg-bot/img_1.png", 'rb')
    )


application.add_handler(CommandHandler("start", start))

application.run_polling()
