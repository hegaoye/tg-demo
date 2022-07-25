import logging

from telegram import Update
from telegram.ext import CallbackContext

from tgbot.api.bet_api_client import BetApiClient
from tgbot.commands.app_command_handler import AppCommandHandler
from tgbot.commands.commands import Command
from tgbot.commands.help_command_handler import HelpCommandHandler
from tgbot.commands.my_bet_command_handler import MyBetCommandHandler
from tgbot.service.bet_order_service import BetOrderService


class GameContextHandler:
    """
    游戏中的所有命令拦截
    """

    def __init__(self):
        self.bet_order_service = BetOrderService()
        self.bet_api_client = BetApiClient()
        self.app_command_handler = AppCommandHandler()
        self.help_command_handler = HelpCommandHandler()
        self.my_bet_command_handler = MyBetCommandHandler()

    async def handle(self, update: Update, context: CallbackContext):
        """
        the callback for handling start command
        """

        text = update.message.text

        logging.info("收到消息：%s", text)
        logging.info("GameContextHandler:%s", update.effective_user.id)
        logging.info("GameContextHandler:%s", update.effective_user.username)
        logging.info("GameContextHandler:%s", update.effective_chat.id)

        bot = context.bot
        bot_id = bot.id
        chat_id = update.effective_chat.id
        user_id = update.effective_user.id

        if text.__eq__(Command.APPLET_KEYBOARD.value):
            # 小程序命令
            await self.app_command_handler.handle(update, context)

        elif text.__eq__(Command.QUERY_BET_KEYBOARD.value):
            # 我投注的订单详情命令
            await self.my_bet_command_handler.handle(update, context)

        elif text.__eq__(Command.HELP_KEYBOARD.value):
            # 帮助命令
            await self.help_command_handler.handle(update, context)

        else:
            # 投注命令
            if not text.startswith("/"):
                return

            # 檢查是否封盤，或者暫停
            is_start = self.bet_api_client.check_status(chat_id, bot_id)
            if not is_start:
                await update.message.reply_text('封盘或者暂停游戏无法投注.')
                return

            bet_num = None
            if text.__eq__(Command.BIG_KEYBOARD.value):
                # 投注金额
                bet_money = 50
                bet_code = Command.BIG.name
            elif text.__eq__(Command.SMALL_KEYBOARD.value):
                # 投注金额
                bet_money = 50
                bet_code = Command.SMALL.name
            elif text.__eq__(Command.ODD_KEYBOARD.value):
                # 投注金额
                bet_money = 50
                bet_code = Command.ODD.name
            elif text.__eq__(Command.EVEN_KEYBOARD.value):
                # 投注金额
                bet_money = 50
                bet_code = Command.EVEN.name
            else:
                bet_code, bet_money, bet_num = Command.INSTANCE.custom_bet(text)
                logging.info("自定义指令投注：%s %s %s", bet_code, bet_money, bet_num)

                if not bet_code:
                    logging.warning("投注非法 %s", text)
                    return

            # 投注
            is_build, error = self.bet_order_service.build(chat_id, user_id, bet_code, bot_id, bet_money, bet_num)
            if is_build:
                # 查询投注详情
                bet_detail = self.bet_order_service.get(chat_id, user_id, bot_id)
                await update.message.reply_text(bet_detail)
            else:
                await update.message.reply_text(error)
