from telegram import Update
from telegram.ext import CallbackContext

from tgbot.commands.base_handler import BaseHandler


class AppCommandHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)

    async def handle(self, update: Update, context: CallbackContext):
        """
        小程序
        :param update:
        :param context:
        :return:
        """
        await context.bot.send_game(chat_id=update.effective_chat.id, game_short_name=self.game_short_name)
