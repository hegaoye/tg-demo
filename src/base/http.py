# coding=utf-8
import json
from urllib import request

from src.base.log4py import logger
from src.base.r import R


def get(url, token=None):
    """
    get 请求
    :param url: 地址
    :return: R
    """
    return __request(url, method='GET', token=token)


def post(url, data=None, token=None):
    """
    post 请求
    :param url: 地址
    :param data: 数据
    :return: R
    """
    return __request(url, method='POST', token=token, data=data)


def put(url, data=None, token=None):
    """
    post 请求
    :param url: 地址
    :param data: 数据
    :return: R
    """
    return __request(url, method='PUT', token=token, data=data)


def __request(url, method, token, data=None) -> R:
    """
    请求
    :param url: 地址
    :param method: 方法
    :param headers: 请求头
    :param data: 数据
    :return: R
    """
    try:
        logger.info("请求url =====> %s ", url)
        if not token:
            token = 'token'

        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }
        if data:
            request_data = __convert_data(data)
            req = request.Request(url, data=request_data, method=method, headers=headers)
        else:
            req = request.Request(url, method=method, headers=headers)

        response = request.urlopen(req)
        result = response.read().decode(encoding='utf-8')
        # 權限token
        authorization_token = response.headers['Authorization']

        logger.info("请求响应 <===== %s", str(result))
        beanret = R().to_obj(result)
        beanret.token = authorization_token
        return beanret
    except Exception as e:
        logger.error(e)
        return R(success=False)


def __convert_data(data) -> str:
    """
    请求数据类型转化
    :param data: 数据
    """
    if isinstance(data, str):
        param = data
    elif isinstance(data, dict):
        param = json.dumps(data).encode('utf-8')
    elif isinstance(data, list):
        param = json.dumps(data).encode('utf-8')
    elif isinstance(data, object):
        param = json.dumps(data.__dict__).encode('utf-8')

    logger.info("请求参数-%s ", param)
    return param
