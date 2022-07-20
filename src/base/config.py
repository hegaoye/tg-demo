import configparser
import os

from settings import SYS_CONF


class Config:
    """
    读取conf配置文件
    """

    def __init__(self, conf=SYS_CONF):
        _basedir = os.path.abspath(os.path.dirname(__file__))
        sys_conf = os.path.join(_basedir, conf)
        cf = configparser.ConfigParser()
        cf.read(sys_conf)
        self.cf = cf

    def read(self, key, value):
        return str(self.cf.get(key, value))
