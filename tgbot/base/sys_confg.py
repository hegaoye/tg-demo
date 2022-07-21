from tgbot.base.config import Config
from tgbot.base.log4py import logger


class SysConf:
    """
    read sys config
    """

    def __init__(self):
        self.__config()

    def __config(self):
        try:
            cfg = Config()
            self.host = cfg.read("sys", "server_host")
            self.bot_token = cfg.read("sys", "bot_token")
            self.begain_words = cfg.read("sys", "begain_words")
            self.game_short_name = cfg.read("sys", "game_short_name")
            self.game_url = cfg.read("sys", "game_url")
            self.group_id = cfg.read("sys", "group_id")
        except Exception as e:
            logger.error("sys-sample.conf 找不到錯誤-%s", e)
