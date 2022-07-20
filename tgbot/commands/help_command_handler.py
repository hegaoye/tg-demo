from telegram import Update
from telegram.ext import CallbackContext

from tgbot.base.sys_confg import SysConf


class HelpCommandHandler:
    def __init__(self):
        self.sys_conf = SysConf()

    async def handle(self, update: Update, context: CallbackContext):
        """
       message to handle any "Option [0-9]" Regrex.
       """
        # sending the reply message with the selected option

        username = update.effective_user.username
        await update.message.reply_text("@" + username + " 点击了 '%s'" % update.message.text)
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("/Users/watson/PycharmProjects/tg-bot/img_1.png", 'rb')
        )