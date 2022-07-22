import logging

from telegram import Update
from telegram.ext import CallbackContext

from tgbot.api.bet_api_client import BetApiClient
from tgbot.base.sys_confg import SysConf
from tgbot.commands.commands import Command
from tgbot.commands.help_command_handler import HelpCommandHandler
from tgbot.service.bet_order_service import BetOrderService


class GameContextHandler:
    """
    游戏中的所有命令拦截
    """

    def __init__(self):
        self.sys_conf = SysConf()
        self.bet_order_service = BetOrderService()
        self.bet_api_client = BetApiClient()

    async def handle(self, update: Update, context: CallbackContext):
        """
        the callback for handling start command
        """

        click_button_text = update.message.text

        logging.info("收到消息：%s", click_button_text)
        logging.info("GameContextHandler:%s", update.effective_user.id)
        logging.info("GameContextHandler:%s", update.effective_user.username)
        logging.info("GameContextHandler:%s", update.effective_chat.id)

        bot = context.bot
        bot_id = bot.id
        chat_id = update.effective_chat.id
        user_id = update.effective_user.id

        if click_button_text.__eq__(Command.APPLET.value):
            await bot.send_game(chat_id=chat_id, game_short_name=self.sys_conf.game_short_name)

        elif click_button_text.__eq__(Command.QUERY_BET.value):
            # 查询投注详情
            bet_detail = self.bet_order_service.get(chat_id, user_id, bot_id)
            await update.message.reply_text(bet_detail)

        elif click_button_text.__eq__(Command.HELP_CN.value):
            await HelpCommandHandler().handle(update, context)

        else:
            # 檢查是否封盤，或者暫停
            is_start = self.bet_api_client.check_status(chat_id, bot_id)
            if not is_start:
                await update.message.reply_text('封盘或者暂停游戏无法投注.')
                return

            if click_button_text.__eq__(Command.BIG.value):
                # 投注金额
                bet_money = 50
            elif click_button_text.__eq__(Command.SMALL.value):
                # 投注金额
                bet_money = 50
            elif click_button_text.__eq__(Command.ODD.value):
                # 投注金额
                bet_money = 50
            elif click_button_text.__eq__(Command.EVEN.value):
                # 投注金额
                bet_money = 50
            else:
                return

            # 投注
            is_build, error = self.bet_order_service.build(chat_id, user_id, Command.BIG.name, bot_id, bet_money)
            if is_build:
                # 查询投注详情
                bet_detail = self.bet_order_service.get(chat_id, user_id, bot_id)
                await update.message.reply_text(bet_detail)
            else:
                await update.message.reply_text(error)
