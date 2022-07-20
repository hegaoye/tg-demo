from enum import Enum


class Command(Enum):
    """
            ['/大 50', '/小 50', '/单 50', '/双 50'],
            ['/查看投注', '/小程序', '/帮助']
    """

    APPLET = "/小程序"
    QUERY_BET = "/查看投注"
    HELP_CN = "/帮助"
    BIG = "/大 50"
    SMALL = "/小 50"
    ODD = "/单 50"
    EVEN = "/双 50"
    START = "start"
    STOP = "stop"
    HELP_EN = "help"
