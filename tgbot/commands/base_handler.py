from tgbot.api.bot_api_client import BotApiClient
from tgbot.api.group_api_client import GroupApiClient
from tgbot.base.singleton import Singleton
from tgbot.base.sys_confg import SysConf


class BaseHandler(Singleton):
    def __init__(self):
        self.sys_conf = SysConf()
        self.bot_name = self.sys_conf.bot_name
        self.bot_token = None
        self.begin_words = None
        self.game_short_name = None
        self.game_url = None
        self.group_id = None

        self.__init_data__()

    def __init_data__(self):
        """
        拉取信息
        """
        # 機器人信息
        bot_api_client = BotApiClient()
        bot= bot_api_client.get(self.bot_name)
        self.bot_token = bot["tgToken"]

        # 群信息
        group_api_client = GroupApiClient()
        group = group_api_client.get_group(bot["id"])
        self.group_id = group["tgGroupId"]
        self.begin_words = group["gameSummary"]
        self.game_short_name = group["tgGameCode"]
        self.game_url = group["domain"]


baseHandler = BaseHandler()
