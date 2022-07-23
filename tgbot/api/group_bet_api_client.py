import logging

from tgbot.api.api_url_enum import Api
from tgbot.base import http
from tgbot.base.return_code import ResponseCode
from tgbot.base.singleton import Singleton
from tgbot.base.sys_confg import SysConf


class GroupBetApiClient(Singleton):
    def __init__(self):
        self.sys_conf = SysConf()
        self.__host = self.sys_conf.host

    def get_group_both_sides(self, group_id) -> dict:
        """
        獲取兩面盤投注信息，用於鍵盤價格設置
        :param group_id: 群id
        """
        url = Api.GET_BOTHSIDES_URL.value.format(host=self.__host, group_id=group_id)
        logging.info('獲取兩面盤投注信息，用於鍵盤價格設置,url=====> %s', url)
        try:
            beanret = http.get(url)
            logging.info('獲取兩面盤投注信息，用於鍵盤價格設置 <===== %s', beanret)

            if beanret.code.__eq__(ResponseCode.Success.value):
                return beanret.data
        except Exception as e:
            logging.error("獲取兩面盤投注信息，用於鍵盤價格設置发生错误={}", e)

        return None
