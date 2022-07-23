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
            return Command.EVEN.name, bet_money, bet_num


if __name__ == '__main__':
    print(Command.INSTANCE.value[0])
    print(Command.INSTANCE.value[1])
    print(Command.INSTANCE.bet("/big 100"))
    print(Command.INSTANCE.bet("/num 123 100"))
