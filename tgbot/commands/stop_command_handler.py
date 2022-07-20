from telegram import Update, ReplyKeyboardRemove
from telegram.ext import CallbackContext

from tgbot.base.sys_confg import SysConf


class StopCommandHandler:
    def __init__(self):
        self.sys_conf = SysConf()

    async def handle(self, update: Update, context: CallbackContext):
        """
        method to handle /remove command to remove the keyboard and return back to text reply
        """

        # making a reply markup to remove keyboard
        # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardremove.html
        reply_markup = ReplyKeyboardRemove()

        # sending the reply so as to remove the keyboard
        await update.message.reply_text(text="暂停游戏", reply_markup=reply_markup)
