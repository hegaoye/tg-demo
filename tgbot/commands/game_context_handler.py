import logging

from telegram import Update
from telegram.ext import CallbackContext

from tgbot.base.sys_confg import SysConf
from tgbot.commands.commands import Command
from tgbot.commands.help_command_handler import HelpCommandHandler


class GameContextHandler:
    def __init__(self):
        self.sys_conf = SysConf()

    async def handle(self, update: Update, context: CallbackContext):
        """
        the callback for handling start command
        """
        issue = """
        第20220720888期合计投注:
        大:{big}
        小:{small}
        单:{even}
        双:{odd}
        号码:{num}
        {at}
        """
        click_button_text = update.message.text
        logging.info("收到消息：%s", click_button_text)
        logging.info("GameContextHandler:%s",update.effective_user.id)
        logging.info("GameContextHandler:%s",update.effective_user.username)

        if click_button_text.__eq__(Command.APPLET.value):
            await context.bot.send_game(
                chat_id=update.effective_chat.id,
                game_short_name=self.sys_conf.game_short_name
            )
        elif click_button_text.__eq__(Command.BIG.value):
            username = update.effective_user.username
            text = issue.format(at="@" + username, big="50", small="0", even="0", odd="0", num="无")
            await update.message.reply_text(text)
        elif click_button_text.__eq__(Command.SMALL.value):
            username = update.effective_user.username
            text = issue.format(at="@" + username, big="0", small="50", even="0", odd="0", num="无")
            await update.message.reply_text(text)
        elif click_button_text.__eq__(Command.ODD.value):
            username = update.effective_user.username
            text = issue.format(at="@" + username, big="0", small="0", even="50", odd="0", num="无")
            await update.message.reply_text(text)
        elif click_button_text.__eq__(Command.EVEN.value):
            username = update.effective_user.username
            text = issue.format(at="@" + username, big="0", small="0", even="0", odd="50", num="无")
            await update.message.reply_text(text)
        elif click_button_text.__eq__(Command.QUERY_BET.value):
            username = update.effective_user.username
            await update.message.reply_text("@" + username + " 点击了 '%s'" % update.message.text + "，查询投注中，请稍等")
        elif click_button_text.__eq__(Command.HELP_CN.value):
            await HelpCommandHandler().handle(update, context)
