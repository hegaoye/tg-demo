class BetOrder:
    def __init__(self, tg_group_id, tg_user_id, bot_id, bet_code, amount, bet_num=None):
        self.tg_group_id = tg_group_id
        self.tg_user_id = tg_user_id
        self.bot_id = bot_id
        self.bet_code = bet_code
        self.bet_num = bet_num
        self.amount = amount
