from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from tgbot.base.sys_confg import SysConf
from tgbot.commands.callback_handler import CallbackHandler
from tgbot.commands.commands import Command
from tgbot.commands.game_context_handler import GameContextHandler
from tgbot.commands.help_command_handler import HelpCommandHandler
from tgbot.commands.member_handler import MemberJoinOrLeftGroupHandler
from tgbot.commands.start_command_handler import StartCommandHandler
from tgbot.commands.stop_command_handler import StopCommandHandler


class BotService:

    def __init__(self):
        self.sys_conf = SysConf()
        self.application = Application.builder().token(self.sys_conf.bot_token).build()

    def run(self):
        """
        启动
        :return:
        """
        self.application.add_handler(CommandHandler(Command.START.value, StartCommandHandler().handle))
        self.application.add_handler(CommandHandler(Command.STOP.value, StopCommandHandler().handle))
        self.application.add_handler(CommandHandler(Command.HELP_EN.value, HelpCommandHandler().handle))

        self.application.add_handler(CallbackQueryHandler(CallbackHandler().handle))
        self.application.add_handler(MessageHandler(filters.TEXT, callback=GameContextHandler().handle))
        self.application.add_handler(MessageHandler(filters.CHAT, callback=MemberJoinOrLeftGroupHandler().handle))

        self.application.run_polling()
