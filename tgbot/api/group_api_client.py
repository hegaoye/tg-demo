import logging

from tgbot.api.api_url_enum import Api
from tgbot.base import http
from tgbot.base.return_code import ResponseCode
from tgbot.base.sys_confg import SysConf


class GroupApiClient:
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

            if not beanret.code.__eq__(ResponseCode.Success.value) and not beanret.data:
                return True
        except Exception as e:
            logging.error("檢查群是否合法发生错误={}", e)
            return False
