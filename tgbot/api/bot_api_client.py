import logging

from tgbot.api.api_url_enum import Api
from tgbot.base import http
from tgbot.base.return_code import ResponseCode
from tgbot.base.singleton import Singleton
from tgbot.base.sys_confg import SysConf


class BotApiClient(Singleton):
    def __init__(self):
        self.sys_conf = SysConf()
        self.__host = self.sys_conf.host

    def get(self, bot_name) -> dict:
        """
        獲取機器人
        """
        url = Api.GET_BOT_URL.value.format(host=self.__host, bot_name=bot_name)
        logging.info('獲取機器人,url=====> %s', url)
        try:
            beanret = http.get(url)
            logging.info('獲取機器人 <===== %s', beanret)

            if not beanret.code.__eq__(ResponseCode.Success.value):
                return beanret.data

        except Exception as e:
            logging.error("獲取機器人发生错误={}", e)

        return None
