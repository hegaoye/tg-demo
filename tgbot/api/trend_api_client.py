import logging

from tgbot.api.api_url_enum import Api
from tgbot.base import http
from tgbot.base.return_code import ResponseCode
from tgbot.base.singleton import Singleton
from tgbot.base.sys_confg import SysConf


class TrendApiClient(Singleton):
    def __init__(self):
        self.sys_conf = SysConf()
        self.__host = self.sys_conf.host

    def get_count(self, chat_id) -> list:
        """
        查看走势统计
        """
        url = Api.TREND_TABLE_URL.value.format(host=self.__host, group_id=chat_id)
        logging.info('查看走势统计,url=====> %s', url)
        try:
            beanret = http.get(url)
            logging.info('查看走势统计 <===== %s', beanret)

            if beanret.code.__eq__(ResponseCode.Success.value):
                return beanret.data

        except Exception as e:
            logging.error("查看走势统计发生错误={}", e)

        return []
