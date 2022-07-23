from telegram import Update
from telegram.ext import CallbackContext

from tgbot.commands.base_handler import BaseHandler
from tgbot.service.bet_order_service import BetOrderService


class MyBetCommandHandler(BaseHandler):
    def __init__(self):
        BaseHandler.__init__(self)
        self.bet_order_service = BetOrderService()

    async def handle(self, update: Update, context: CallbackContext):
        """
        小程序
        :param update:
        :param context:
        :return:
        """
        bot = context.bot
        bot_id = bot.id
        chat_id = update.effective_chat.id
        user_id = update.effective_user.id

        # 查询投注详情
        bet_detail = self.bet_order_service.get(chat_id, user_id, bot_id)
        await update.message.reply_text(bet_detail)
