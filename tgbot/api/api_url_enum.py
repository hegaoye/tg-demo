from enum import Enum


class Api(Enum):
    """
    api 枚舉
    """

    """
    创建用户 post
    """
    USER_BUILD_URL = "{host}/user/build"

    """
    创建投注订单 post
    """
    BET_ORDER_BUILD_URL = "{host}/betOrder/build"

    """
    查询订单详情
    """
    GET_BET_ORDER_URL = "{host}/betOrder/load/{group_id}/{user_id}/{bot_id}"
