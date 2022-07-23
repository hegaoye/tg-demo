import re
from enum import Enum


class Command(Enum):
    """
            ['/大 50', '/小 50', '/单 50', '/双 50'],
            ['/查看投注', '/小程序', '/帮助']
    """

    APPLET_KEYBOARD = "/小程序"
    QUERY_BET_KEYBOARD = "/查看投注"
    HELP_KEYBOARD = "/帮助"

    BIG_KEYBOARD = "/大 {bet_money}"
    SMALL_KEYBOARD = "/小 {bet_money}"
    ODD_KEYBOARD = "/单 {bet_money}"
    EVEN_KEYBOARD = "/双 {bet_money}"

    NUM = "num"
    BIG = "big"
    SMALL = "small"
    ODD = "odd"
    EVEN = "even"

    NUM_CN = "/号码"
    BIG_CN = "/大"
    SMALL_CN = "/小"
    ODD_CN = "/单"
    EVEN_CN = "/双"

    START = "start"
    STOP = "stop"
    HELP_EN = "help"
    BYE = "bye"
    APP = "app"
    MY_BET = "my"

    INSTANCE = None

    def bet(self, text):
        """
        投注拆分
        :param text: 投注指令 /big 100 ,/num 123 100
        :return:
        """
        text_arr = str(text).split(" ")
        bet_money = text_arr[1]
        if text.__contains__(Command.BIG.value):
            return Command.BIG.name, bet_money, None
        elif text.__contains__(Command.SMALL.value):
            return Command.SMALL.name, bet_money, None
        elif text.__contains__(Command.ODD.value):
            return Command.ODD.name, bet_money, None
        elif text.__contains__(Command.EVEN.value):
            return Command.EVEN.name, bet_money, None
        elif text.__contains__(Command.NUM.value):
            bet_num = text_arr[1]
            bet_money = text_arr[2]
            return Command.NUM.name, bet_money, bet_num

    def custom_bet(self, text):
        """
        自定义命令匹配
        :param text:消息
        :return: 分离投注结果
        """
        searchObj = re.search(r'(/(大|小|单|双)\s\d{1,3})|(/号码\s\d{0,9}\s\d{1,3})', text, re.M | re.I)
        if searchObj:
            text_arr = str(text).split(" ")
            bet_money = text_arr[1]
            if text.__contains__(Command.BIG_CN.value):
                return Command.BIG.name, bet_money, None
            elif text.__contains__(Command.SMALL_CN.value):
                return Command.SMALL.name, bet_money, None
            elif text.__contains__(Command.ODD_CN.value):
                return Command.ODD.name, bet_money, None
            elif text.__contains__(Command.EVEN_CN.value):
                return Command.EVEN.name, bet_money, None
            elif text.__contains__(Command.NUM_CN.value):
                bet_num = text_arr[1]
                bet_money = text_arr[2]
                return Command.NUM.name, bet_money, bet_num
        else:
            return None, None, None

    def key(self, bet_money):
        """
        格式化按鍵
        :param bet_money:投注額度
        """
        return str(self.value).format(bet_money=bet_money)


if __name__ == '__main__':
    # print(Command.INSTANCE.bet("/big 100"))
    print(Command.INSTANCE.bet("/num 123 100"))
    print(Command.INSTANCE.custom_bet("/号码 123 100"))
    print(Command.INSTANCE.custom_bet('/大 100'))
