from telegram import Update, ReplyKeyboardRemove, ReplyKeyboardMarkup, CallbackQuery
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters, CallbackQueryHandler

from src.base.sys_confg import SysConf


class BotService:

    def __init__(self):
        sys_conf = SysConf()
        self.application = Application.builder().token(sys_conf.bot_token).build()

    def run(self):
        """
        启动
        :return:
        """
        self.application.add_handler(CommandHandler("start", self.start))
        self.application.add_handler(CommandHandler("stop", self.stop))
        self.application.add_handler(CommandHandler("help", self.help))

        self.application.add_handler(CallbackQueryHandler(self.button))
        self.application.add_handler(MessageHandler(filters.TEXT, callback=self.send_game_message))
        self.application.run_polling()

    async def start(self, update: Update, context: CallbackContext):
        """
        method to handle the /start command and create keyboard
        """

        # defining the keyboard layout
        kbd_layout = [
            ['/大 50', '/小 50', '/单 50', '/双 50'],
            ['/查看投注', '/小程序', '/帮助']
        ]

        kbd = ReplyKeyboardMarkup(keyboard=kbd_layout, resize_keyboard=True)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="欢迎使用星彩娱乐",
            reply_markup=kbd
        )

    async def stop(self, update: Update, context: CallbackContext):
        """
        method to handle /remove command to remove the keyboard and return back to text reply
        """

        # making a reply markup to remove keyboard
        # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.replykeyboardremove.html
        reply_markup = ReplyKeyboardRemove()

        # sending the reply so as to remove the keyboard
        await update.message.reply_text(text="暂停游戏", reply_markup=reply_markup)

    async def send_game_message(self, update: Update, context: CallbackContext):
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
        print("收到消息：", click_button_text)

        if click_button_text.__eq__('/小程序'):
            await context.bot.send_game(
                chat_id=update.effective_chat.id,
                game_short_name="zijietiaodonggame"
            )
        elif click_button_text.__contains__('/大 50'):
            username = update.effective_user.username
            text = issue.format(at="@" + username, big="50", small="0", even="0", odd="0", num="无")
            await update.message.reply_text(text)
        elif click_button_text.__contains__('/小 50'):
            username = update.effective_user.username
            text = issue.format(at="@" + username, big="0", small="50", even="0", odd="0", num="无")
            await update.message.reply_text(text)
        elif click_button_text.__contains__('/单 50'):
            username = update.effective_user.username
            text = issue.format(at="@" + username, big="0", small="0", even="50", odd="0", num="无")
            await update.message.reply_text(text)
        elif click_button_text.__contains__('/双 50'):
            username = update.effective_user.username
            text = issue.format(at="@" + username, big="0", small="0", even="0", odd="50", num="无")
            await update.message.reply_text(text)
        elif click_button_text.__contains__('/查看投注'):
            username = update.effective_user.username
            await update.message.reply_text("@" + username + " 点击了 '%s'" % update.message.text + "，查询投注中，请稍等")
        elif click_button_text.__contains__('/帮助'):
            self.help(update, context)

    async def button(self, update, context: CallbackContext):
        """
        callback method handling button press
        """
        # documentation: https://python-telegram-bot.readthedocs.io/en/stable/telegram.callbackquery.html
        query: CallbackQuery = update.callback_query

        demo_url = "https://www.wangcai321.com/bot/web/player.html?g=-1001756231525&t=YAyEYzQlNZ2w2Fo1658210341868#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DVQfENQsIeEniRnaKwcQE"
        await query.answer(text="open", url=demo_url)

    async def help(self, update: Update, context: CallbackContext):
        """
        message to handle any "Option [0-9]" Regrex.
        """
        # sending the reply message with the selected option
        username = update.effective_user.username
        await update.message.reply_text("@" + username + " 点击了 '%s'" % update.message.text)
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open("/Users/watson/PycharmProjects/tg-bot/img_1.png", 'rb')
        )
