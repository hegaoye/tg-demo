# coding=utf-8
import time

from telegram.ext import Application

from tgbot.base.sys_confg import SysConf
from tgbot.base.trend_image import trend_image


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

    def __trend_photo(self) -> str:
        data = [['19:00', '9'], ['19:02', '4'], ['19:04', '2'], ['19:06', '5'], ['19:08', '1'], ['19:10', '3'],
                ['19:12', '6'],
                ['19:14', '7'], ['19:16', '5'], ['19:18', '9'], ['19:20', '0'], ['19:22', '7'], ['19:24', '2'],
                ['19:26', '4'],
                ['19:28', '4'], ['19:30', '5'], ['19:32', '6'], ['19:34', '7'], ['19:36', '8'], ['19:38', '9'],
                ['19:40', '0'],
                ['19:42', '1'], ['19:44', '5'], ['19:46', '6'], ['19:48', '4'], ['19:50', '7'], ['19:52', '6'],
                ['19:54', '7'],
                ['19:58', '8']]
        photo_path = trend_image(data)
        return photo_path

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
        bot = self.application.bot
        # 发送走势图片
        photo_path = self.__trend_photo()
        await bot.send_photo(
            chat_id=self.sys_conf.group_id,
            photo=open(photo_path, 'rb'))

        # 发送投注报表
        open_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        await bot.send_message(
            chat_id=self.sys_conf.group_id,
            text=result.format(open_time=open_time))
