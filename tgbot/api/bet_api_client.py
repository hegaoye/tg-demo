import logging

from tgbot.api.api_url_enum import Api
from tgbot.base import http
from tgbot.base.return_code import ResponseCode
from tgbot.base.sys_confg import SysConf


class BetApiClient:
    def __init__(self):
        self.sys_conf = SysConf()
        self.__host = self.sys_conf.host

    def start(self, chat_id, bot_id) -> bool:
        """
        開啟投注
        """
        try:
            url = Api.BET_START_URL.value.format(host=self.__host)
            logging.info('開啟投注,url=====> %s', url)
            data = {
                "groupId": chat_id,
                "botId": bot_id
            }
            beanret = http.put(url, data)
            logging.info('開啟投注,返回信息<===== %s', beanret)
            if beanret.code.__eq__(ResponseCode.Exists.value):
                return True

        except Exception as e:
            logging.error(e)

        return False

    def stop(self, chat_id, bot_id) -> bool:
        """
        關閉投注
        """
        try:
            url = Api.BET_STOP_URL.value.format(host=self.__host)
            logging.info('關閉投注,url=====> %s', url)
            data = {
                "groupId": chat_id,
                "botId": bot_id
            }
            beanret = http.put(url, data)
            logging.info('關閉投注,返回信息<===== %s', beanret)
            if beanret.code.__eq__(ResponseCode.Exists.value):
                return True

        except Exception as e:
            logging.error(e)

        return False

    def check_status(self, chat_id, bot_id) -> bool:
        """
        檢查投注狀態
        :param chat_id: 群id
        :param bot_id: 机器人id
        :return: True 開啟，False 關閉
        """
        url = Api.CHECK_BET_STATUS_URL.value.format(host=self.__host, group_id=chat_id, bot_id=bot_id)
        logging.info('檢查投注狀態,url=====> %s', url)
        try:
            beanret = http.get(url)
            logging.info('檢查投注狀態 <===== %s', beanret)

            if not beanret.code.__eq__(ResponseCode.Success.value) and beanret.data:
                return True

        except Exception as e:
            logging.error("檢查投注狀態发生错误={}", e)

        return False
