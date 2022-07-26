import logging

from tgbot.api.api_url_enum import Api
from tgbot.base import http
from tgbot.base.return_code import ResponseCode
from tgbot.base.singleton import Singleton
from tgbot.base.sys_confg import SysConf


class TokenApiClient(Singleton):
    def __init__(self):
        self.sys_conf = SysConf()
        self.__host = self.sys_conf.host

    def token(self, chat_id, username) -> bool:
        """
        檢查投注狀態
        :param chat_id: 群id
        :return: True 開啟，False 關閉
        """
        url = Api.TOKEN_URL.value.format(host=self.__host, group_id=chat_id, username=username)
        logging.info('檢查投注狀態,url=====> %s', url)
        try:
            beanret = http.get(url)
            logging.info('檢查投注狀態 <===== %s', beanret)

            if beanret.code.__eq__(ResponseCode.Success.value):
                return beanret.data

        except Exception as e:
            logging.error("檢查投注狀態发生错误={}", e)

        return None
