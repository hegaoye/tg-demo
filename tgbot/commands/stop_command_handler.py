from telegram import Update
from telegram.ext import CallbackContext

from tgbot.api.bet_api_client import BetApiClient
from tgbot.commands.base_handler import baseHandler


class StopCommandHandler:
    def __init__(self):
        self.baseHandler = baseHandler
        self.bet_api_client = BetApiClient()

    async def handle(self, update: Update, context: CallbackContext):
        """
        暂停触发
        method to handle /remove command to remove the keyboard and return back to text reply
        reply_markup = ReplyKeyboardRemove()
        await update.message.reply_text(text="暂停游戏", reply_markup=reply_markup)
        """

        username = update.effective_user.username
        bot = context.bot
        bot_id = bot.id
        chat_id = update.effective_chat.id
        is_stop = self.bet_api_client.stop(chat_id, bot_id)
        if is_stop:
            await update.message.reply_text(text="游戏已被 @" + username + " 暂停")
        else:
            await update.message.reply_text(text="封盘中游戏无法暂停，仅投注期间可以暂停游戏 @" + username)
