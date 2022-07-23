from telegram import Update
from telegram.ext import CallbackContext

from tgbot.base.sys_confg import SysConf


class AppCommandHandler:
    def __init__(self):
        self.sys_conf = SysConf()

    async def handle(self, update: Update, context: CallbackContext):
        """
        小程序
        :param update:
        :param context:
        :return:
        """
        await context.bot.send_game(chat_id=update.effective_chat.id, game_short_name=self.sys_conf.game_short_name)
