import logging

from tgbot.api.api_url_enum import Api
from tgbot.base import http
from tgbot.base.return_code import ResponseCode
from tgbot.base.singleton import Singleton
from tgbot.base.sys_confg import SysConf


class BetOrderApiClient(Singleton):
    def __init__(self):
        self.sys_conf = SysConf()
        self.__host = self.sys_conf.host

    def build(self, bet):
        """
        创建投注订单
        :param bet: 投注数据
        """
        try:
            url = Api.BET_ORDER_BUILD_URL.value.format(host=self.__host)
            logging.info('创建tg 投注订单,url=====> %s', url)

            beanret = http.post(url, bet)
            logging.info('创建tg 投注订单,返回信息<===== %s', beanret.to_json())
            if beanret.code.__eq__(ResponseCode.Success.value):
                return True, "投注成功"
            else:
                return False, "投注失败"
        except Exception as e:
            logging.error(e)
            return False, "投注失败"

    def get(self, chat_id, user_id, bot_id) -> str:
        """
        拉取投注详情
        :param chat_id: 群id
        :param user_id: 用户id
        :param bot_id: 机器人id
        :return: 投注详情
        """
        url = Api.GET_BET_ORDER_URL.value.format(host=self.__host, group_id=chat_id, user_id=user_id, bot_id=bot_id)
        logging.info('拉取用戶投注详情,url=====> %s', url)
        try:
            beanret = http.get(url)
            logging.info('拉取用戶投注详情 <===== %s', beanret)

            if beanret.code.__eq__(ResponseCode.Success.value):
                return beanret.data
        except Exception as e:
            logging.error("拉取本机需要启动的容器数量发生错误={}", e)

        return ""

    def bet_order_count(self, chat_id):
        """
        投注订单统计
        """
        url = Api.BET_ORDER_COUNT_URL.value.format(host=self.__host, group_id=chat_id)
        logging.info('投注订单统计,url=====> %s', url)
        try:
            beanret = http.get(url)
            logging.info('投注订单统计 <===== %s', beanret)

            if beanret.code.__eq__(ResponseCode.Success.value):
                return beanret.data
        except Exception as e:
            logging.error("投注订单统计发生错误={}", e)

        return None
