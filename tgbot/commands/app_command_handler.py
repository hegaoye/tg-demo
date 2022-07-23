from telegram import Update
from telegram.ext import CallbackContext

from tgbot.commands.base_handler import baseHandler


class AppCommandHandler:
    def __init__(self):
        self.baseHandler = baseHandler

    async def handle(self, update: Update, context: CallbackContext):
        """
        小程序
        """
        await context.bot.send_game(chat_id=update.effective_chat.id, game_short_name=self.baseHandler.game_short_name)
