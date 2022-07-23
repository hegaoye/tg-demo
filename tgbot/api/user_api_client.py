import logging

from tgbot.api.api_url_enum import Api
from tgbot.base import http
from tgbot.base.return_code import ResponseCode
from tgbot.base.singleton import Singleton
from tgbot.base.sys_confg import SysConf


class UserApiClient(Singleton):
    def __init__(self):
        self.sys_conf = SysConf()
        self.__host = self.sys_conf.host

    def join_group(self, chat_id, bot_id, user_id, username, name) -> str:
        """
        入群
        """
        try:
            url = Api.USER_BUILD_URL.value.format(host=self.__host)
            logging.info('创建tg用户,url=====> %s', url)
            data = {
                "groupId": chat_id,
                "tgBotId": bot_id,
                "tgUserId": user_id,
                "tgUsername": username
            }
            beanret = http.post(url, data)
            logging.info('创建tg用户,返回信息<===== %s', beanret.to_json())
            if beanret.code.__eq__(ResponseCode.Success.value):
                return beanret.data
        except Exception as e:
            logging.error(e)

        return ""

    def left_group(self, chat_id, bot_id, user_id):
        """
        退群
        """
        try:
            url = Api.LEFT_GROUP_URL.value.format(host=self.__host)
            logging.info('退群,url=====> %s', url)
            data = {
                "tgGroupId": chat_id,
                "tgBotId": bot_id,
                "tgUserId": user_id
            }
            beanret = http.put(url, data)

            logging.info('退群,返回信息<===== %s', beanret)
            if beanret.code.__eq__(ResponseCode.Success.value):
                return True

        except Exception as e:
            logging.error(e)

        return False
