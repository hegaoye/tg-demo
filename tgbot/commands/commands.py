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
