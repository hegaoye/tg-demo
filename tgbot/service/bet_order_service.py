from tgbot.api.bet_order_api_client import BetOrderApiClient
from tgbot.models.bet_order import BetOrder


class BetOrderService:
    def __init__(self):
        self.bet_api_client = BetOrderApiClient()

    def build(self, chat_id, user_id, bet_code, bot_id, amount, bet_num=None):
        """
        创建投注单
        :return:
        """
        bet_order = BetOrder(chat_id, user_id, bet_code, bot_id, amount, bet_num)
        return self.bet_api_client.build(bet_order)

    def get(self, chat_id, user_id, bot_id):
        """
        拉取投注详情
        :param chat_id:群id
        :param user_id:用户id
        :param bot_id:机器人id
        :return:详情
        """
        return self.bet_api_client.get(chat_id, user_id, bot_id)
