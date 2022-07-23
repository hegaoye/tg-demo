import logging

from telegram import Update, CallbackQuery
from telegram.ext import CallbackContext

from tgbot.commands.base_handler import baseHandler


class CallbackHandler:
    def __init__(self):
        self.baseHandler = baseHandler

    async def handle(self, update: Update, context: CallbackContext):
        """
        callback method handling button press
        """
        query: CallbackQuery = update.callback_query
        logging.info("CallbackHandler:%s", update.effective_user.id)
        logging.info("CallbackHandler:%s", update.effective_user.username)
        await query.answer(text="open", url=self.game_url)
