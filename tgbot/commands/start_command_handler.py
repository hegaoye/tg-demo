import logging

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

from tgbot.api.bet_api_client import BetApiClient
from tgbot.api.group_api_client import GroupApiClient
from tgbot.commands.base_handler import BaseHandler, baseHandler
from tgbot.commands.commands import Command


class StartCommandHandler:
    def __init__(self):
        self.baseHandler = baseHandler
        self.group_api_client = GroupApiClient()
        self.bet_api_client = BetApiClient()

    async def handle(self, update: Update, context: CallbackContext):
        """
        method to handle the /start command and create keyboard
        """

        logging.info(self.baseHandler.begin_words)
        logging.info("StartCommandHandler:%s", update.effective_user.id)
        logging.info("StartCommandHandler:%s", update.effective_user.username)

        username = update.effective_user.username
        bot = context.bot
        bot_id = bot.id
        chat_id = update.effective_chat.id
        is_legal = self.group_api_client.check_group_is_legal(chat_id, bot_id)
        if not is_legal:
            # todo 不合法自動退出當前群操作
            return

        # 开启投注
        self.bet_api_client.start(chat_id, bot_id)

        # 键盘布局
        kbd_layout = [
            [Command.BIG_KEYBOARD.value, Command.SMALL_KEYBOARD.value, Command.ODD_KEYBOARD.value,
             Command.EVEN_KEYBOARD.value],
            [Command.QUERY_BET_KEYBOARD.value, Command.APPLET_KEYBOARD.value, Command.HELP_KEYBOARD.value]
        ]

        kbd = ReplyKeyboardMarkup(keyboard=kbd_layout, resize_keyboard=True)

        # 发送消息
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="游戏已被 @" + username + " 开启，可以开始游戏",
                                       reply_markup=kbd)
