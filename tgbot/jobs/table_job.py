# coding=utf-8

from telegram.ext import Application

from tgbot.api.bet_order_api_client import BetOrderApiClient
from tgbot.api.trend_api_client import TrendApiClient
from tgbot.base.sys_confg import SysConf
from tgbot.base.trend_image import trend_image
from tgbot.commands.base_handler import baseHandler


class TableJob:
    """
    启动检测 pod 存活 任务
    """

    def __init__(self):
        self.sys_conf = SysConf()
        self.baseHandler = baseHandler
        self.trend_api_client = TrendApiClient()
        self.bet_order_api_client = BetOrderApiClient()
        self.application = Application.builder().token(self.sys_conf.bot_token).build()

    async def run(self):
        """
        运行入口
        """
        await self.run_task()

    def __trend_photo(self) -> str:
        """
        绘制走势图
        """
        # data = [['19:00', '9'], ['19:02', '4'], ['19:04', '2'], ['19:06', '5'], ['19:08', '1'], ['19:10', '3'],
        #         ['19:12', '6'],
        #         ['19:14', '7'], ['19:16', '5'], ['19:18', '9'], ['19:20', '0'], ['19:22', '7'], ['19:24', '2'],
        #         ['19:26', '4'],
        #         ['19:28', '4'], ['19:30', '5'], ['19:32', '6'], ['19:34', '7'], ['19:36', '8'], ['19:38', '9'],
        #         ['19:40', '0'],
        #         ['19:42', '1'], ['19:44', '5'], ['19:46', '6'], ['19:48', '4'], ['19:50', '7'], ['19:52', '6'],
        #         ['19:54', '7'],
        #         ['19:58', '8']]

        data = self.trend_api_client.get_count(self.baseHandler.group_id)
        photo_path = trend_image(data)
        return photo_path

    async def run_task(self):
        """
        运行入口
        """
        bot = self.application.bot

        # 发送走势图片
        photo_path = self.__trend_photo()
        await bot.send_photo(chat_id=self.baseHandler.group_id, photo=open(photo_path, 'rb'))

        # 发送投注报表
        result = self.bet_order_api_client.bet_order_count(self.baseHandler.group_id)
        await bot.send_message(chat_id=self.baseHandler.group_id, text=result)
