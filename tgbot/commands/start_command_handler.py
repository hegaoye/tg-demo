import logging

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

from tgbot.base.sys_confg import SysConf
from tgbot.commands.commands import Command


class StartCommandHandler:
    def __init__(self):
        self.sys_conf = SysConf()

    async def handle(self, update: Update, context: CallbackContext):
        """
        method to handle the /start command and create keyboard
        """

        logging.info(self.sys_conf.begain_words)
        logging.info("StartCommandHandler:%s", update.effective_user.id)
        logging.info("StartCommandHandler:%s", update.effective_user.username)

        # 键盘布局
        kbd_layout = [
            [Command.BIG.value, Command.SMALL.value, Command.ODD.value, Command.EVEN.value],
            [Command.QUERY_BET.value, Command.APPLET.value, Command.HELP_CN.value]
        ]

        kbd = ReplyKeyboardMarkup(keyboard=kbd_layout, resize_keyboard=True)

        # 发送消息
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=self.sys_conf.begain_words,
            reply_markup=kbd
        )
