import logging

from telegram import Update, CallbackQuery
from telegram.ext import CallbackContext

from tgbot.api.token_api_client import TokenApiClient
from tgbot.commands.base_handler import baseHandler


class AppCallbackHandler:
    def __init__(self):
        self.baseHandler = baseHandler
        self.token_api_client = TokenApiClient()

    async def handle(self, update: Update, context: CallbackContext):
        """
        app 命令跳轉
        """
        query: CallbackQuery = update.callback_query
        logging.info("CallbackHandler:%s", update.effective_user.id)
        logging.info("CallbackHandler:%s", update.effective_user.username)
        chat_id = update.effective_chat.id
        username = update.effective_user.username
        token = self.token_api_client.token(chat_id, username)
        game_url = self.baseHandler.game_url + "?token=" + token + "&username=" + username
        if game_url:
            await query.answer(text="open", url=game_url)
        else:
            await query.answer(text="open", url=self.baseHandler.game_url)
