from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from tgbot.commands.base_handler import baseHandler


class ByeCommandHandler:
    def __init__(self):
        self.baseHandler = baseHandler

    async def handle(self, update: Update, context: CallbackContext):
        """
       message to handle any "Option [0-9]" Regrex.
       """
        reply_markup = ReplyKeyboardRemove()
        await update.message.reply_text(text="移除键盘", reply_markup=reply_markup)
