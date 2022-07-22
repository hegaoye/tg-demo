import logging

from tgbot.api.api_url_enum import Api
from tgbot.base import http
from tgbot.base.return_code import ResponseCode
from tgbot.base.sys_confg import SysConf


class UserApiClient:
    def __init__(self):
        self.sys_conf = SysConf()
        self.__host = self.sys_conf.host

    def build(self, user):
        """
        创建用户
        :param user: 用户数据
        """
        try:
            url = Api.USER_BUILD_URL.value.format(host=self.__host)
            logging.info('创建tg用户,url=====> %s', url)

            beanret = http.post(url, user)
            logging.info('创建tg用户,返回信息<===== %s', beanret.to_json())
            if beanret.code.__eq__(ResponseCode.Exists.value):
                pass
        except Exception as e:
            logging.error(e)
