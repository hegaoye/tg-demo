from enum import Enum


class ResponseCode(Enum):
    """
    响应类型编码
    """
    Success = "0000"
    Exists = "9005"
    BET_LOCK = "1003"
