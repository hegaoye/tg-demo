# coding=utf-8
import time

from telegram.ext import Application

from tgbot.base.sys_confg import SysConf


class TableJob:
    """
    启动检测 pod 存活 任务
    """

    def __init__(self):
        self.sys_conf = SysConf()
        self.application = Application.builder().token(self.sys_conf.bot_token).build()

    async def run(self):
        """
        运行入口
        """
        await self.run_task()

    async def run_task(self):
        """
        运行入口
        """
        result = """
        第202207201918期
BTC/USDT: 23673.6
7 , 大 , 单
盈亏统计：
无人投注

第202207201920期
开奖时间：{open_time}
投注中...
本期枱红 10000 试玩
两面赔率 1.96
大小限红 10 ~ 1000
单双限红 10 ~ 1000
号码赔率 9.8
号码限红 10 ~ 500
        """
        open_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        bot = self.application.bot
        await bot.send_photo(
            chat_id="-1001713031902",
            photo=open("/Users/watson/PycharmProjects/tg-demo2/images/table.jpg", 'rb'))

        await bot.send_message(
            chat_id="-1001713031902",
            text=result.format(open_time=open_time))
