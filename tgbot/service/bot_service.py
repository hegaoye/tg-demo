from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler

from tgbot.base.sys_confg import SysConf
from tgbot.commands.app_command_handler import AppCommandHandler
from tgbot.commands.bet_command_handler import BetCommandHandler
from tgbot.commands.bye_command_handler import ByeCommandHandler
from tgbot.commands.app_callback_handler import AppCallbackHandler
from tgbot.commands.commands import Command
from tgbot.commands.game_context_handler import GameContextHandler
from tgbot.commands.help_command_handler import HelpCommandHandler
from tgbot.commands.member_handler import MemberJoinOrLeftGroupHandler
from tgbot.commands.my_bet_command_handler import MyBetCommandHandler
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
        # start 命令监听
        self.application.add_handler(CommandHandler(Command.START.value, StartCommandHandler().handle))

        # stop 命令监听
        self.application.add_handler(CommandHandler(Command.STOP.value, StopCommandHandler().handle))

        # help 命令监听
        self.application.add_handler(CommandHandler(Command.HELP_EN.value, HelpCommandHandler().handle))

        # 移除机器人
        self.application.add_handler(CommandHandler(Command.BYE.value, ByeCommandHandler().handle))

        # 小程序
        self.application.add_handler(CommandHandler(Command.APP.value, AppCommandHandler().handle))

        # 我的订单
        self.application.add_handler(CommandHandler(Command.MY_BET.value, MyBetCommandHandler().handle))

        # 投注 大，小，单，双，数字 命令监听
        self.application.add_handler(CommandHandler(Command.BIG.value, BetCommandHandler().handle))
        self.application.add_handler(CommandHandler(Command.SMALL.value, BetCommandHandler().handle))
        self.application.add_handler(CommandHandler(Command.ODD.value, BetCommandHandler().handle))
        self.application.add_handler(CommandHandler(Command.EVEN.value, BetCommandHandler().handle))
        self.application.add_handler(CommandHandler(Command.NUM.value, BetCommandHandler().handle))

        # 自定义键盘事件监听
        self.application.add_handler(MessageHandler(filters.TEXT, callback=GameContextHandler().handle))

        # 群异动监听，加入，退出等
        self.application.add_handler(MessageHandler(filters.CHAT, callback=MemberJoinOrLeftGroupHandler().handle))

        # 小程序跳轉
        self.application.add_handler(CallbackQueryHandler(AppCallbackHandler().handle))

        self.application.run_polling()
