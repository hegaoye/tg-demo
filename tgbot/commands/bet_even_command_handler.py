from telegram import Update
from telegram.ext import CallbackContext

from tgbot.base.sys_confg import SysConf
from tgbot.commands.base_handler import BaseHandler


class BetCommandHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)

    async def handle(self, update: Update, context: CallbackContext):
        """
       message to handle any "Option [0-9]" Regrex.
       """
        # sending the reply message with the selected option

        # todo 處理 大小，單雙，數字等投注
        username = update.effective_user.username
        await update.message.reply_text("@" + username + " 以下是使用指南")
