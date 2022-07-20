from telegram import Update, Bot, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo, CallbackGame, CallbackQuery
from telegram.constants import ParseMode
from telegram.ext import CallbackContext, CommandHandler, Application, CallbackQueryHandler

application = Application.builder().token("5512528385:AAFVl3eu7EMoAKIgLyoc3Pmq-wDvRF1vf40").arbitrary_callback_data(
    True).build()


async def start(update: Update, context: CallbackContext):
    """
    the callback for handling start command
    """
    await context.bot.send_game(
        chat_id=update.effective_chat.id,
        game_short_name="juncaixingchigame"
    )


async def button(update, context: CallbackContext):
    """
    callback method handling button press
    """
    # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html
    query: CallbackQuery = update.callback_query

    demo_url = "https://www.wangcai321.com/bot/web/player.html?g=-1001756231525&t=YAyEYzQlNZ2w2Fo1658210341868#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DVQfENQsIeEniRnaKwcQE"
    await query.answer(text="open", url=demo_url)


application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button))  # handling inline buttons pressing

application.run_polling()
