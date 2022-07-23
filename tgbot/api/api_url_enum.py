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
    退群 put
    """
    LEFT_GROUP_URL = "{host}/user/left"

    """
    创建投注订单 post
    """
    BET_ORDER_BUILD_URL = "{host}/betOrder/build"

    """
    查询订单详情 get
    """
    GET_BET_ORDER_URL = "{host}/betOrder/load/{group_id}/{user_id}/{bot_id}"

    """
    投注订单统计
    """
    BET_ORDER_COUNT_URL = "{host}/betOrder/count/{group_id}"

    """
    查詢群是否存在 get
    """
    GET_GROUP_URL = "{host}/tgGroupBot/load/{group_id}/{bot_id}"

    """
    根據群id後去群信息
    """
    GET_GROUP_BY_ID_URL = "{host}/group/load/id/{group_id}"

    """
    投注開啟 put
    """
    BET_START_URL = "{host}/bet/start/{group_id}/{bot_id}"

    """
    投注關閉 put
    """
    BET_STOP_URL = "{host}/bet/stop/{group_id}/{bot_id}"

    """
    檢查投注狀態 get
    """
    CHECK_BET_STATUS_URL = "{host}/bet/status/{group_id}/{bot_id}"

    """
    走势图统计 get
    """
    TREND_TABLE_URL = "{host}/trendRecord/count/{group_id}"

    """
    獲取機器人 get
    """
    GET_BOT_URL = "{host}/bot/load/name/{bot_name}"
