import logging

from tgbot.api.api_url_enum import Api
from tgbot.base import http
from tgbot.base.return_code import ResponseCode
from tgbot.base.singleton import Singleton
from tgbot.base.sys_confg import SysConf


class GroupApiClient(Singleton):
    def __init__(self):
        self.sys_conf = SysConf()
        self.__host = self.sys_conf.host

    def check_group_is_legal(self, chat_id, bot_id) -> bool:
        """
        檢查群是否合法
        """
        url = Api.GET_GROUP_URL.value.format(host=self.__host, group_id=chat_id, bot_id=bot_id)
        logging.info('檢查群是否合法,url=====> %s', url)
        try:
            beanret = http.get(url)
            logging.info('檢查群是否合法 <===== %s', beanret)

            if beanret.code.__eq__(ResponseCode.Success.value):
                return True, beanret.data
        except Exception as e:
            logging.error("檢查群是否合法发生错误={}", e)

        return False, None

    def get_group(self, group_id) -> dict:
        """
        獲取群詳情
        :param group_id: 群id
        """
        url = Api.GET_GROUP_BY_ID_URL.value.format(host=self.__host, group_id=group_id)
        logging.info('獲取群詳情,url=====> %s', url)
        try:
            beanret = http.get(url)
            logging.info('獲取群詳情 <===== %s', beanret)

            if beanret.code.__eq__(ResponseCode.Success.value):
                return beanret.data
        except Exception as e:
            logging.error("獲取群詳情发生错误={}", e)

        return None
