import logging

from telegram import Update
from telegram.ext import CallbackContext

from tgbot.commands.base_handler import baseHandler
from tgbot.commands.commands import Command
from tgbot.service.bet_order_service import BetOrderService


class BetCommandHandler:
    def __init__(self):
        self.baseHandler = baseHandler
        self.bet_order_service = BetOrderService()

    async def handle(self, update: Update, context: CallbackContext):
        """
        投注指令處理
        :param update:
        :param context:
        :return:
        """
        bet_text = update.message.text
        bet_code, bet_money, bet_num = Command.INSTANCE.bet(bet_text)
        logging.info("投注信息 %s %s %s", bet_code, bet_money, bet_num)

        bot = context.bot
        bot_id = bot.id
        chat_id = update.effective_chat.id
        user_id = update.effective_user.id
        username = update.effective_user.username
        is_bet, msg = self.bet_order_service.build(chat_id, user_id, bet_code, bot_id, bet_money, bet_num)
        await update.message.reply_text("@" + username + " " + msg)
