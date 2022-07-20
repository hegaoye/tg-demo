import logging

from telegram import Update, CallbackQuery
from telegram.ext import CallbackContext

from tgbot.base.sys_confg import SysConf


class CallbackHandler:
    def __init__(self):
        self.sys_conf = SysConf()

    async def handle(self, update: Update, context: CallbackContext):
        """
        callback method handling button press
        """
        query: CallbackQuery = update.callback_query
        logging.info(update.effective_user.id)
        logging.info(update.effective_user.username)
        await query.answer(text="open", url=self.sys_conf.game_url)
