# coding=utf-8
import logging

from src.service.bot_service import BotService

if __name__ == '__main__':
    logging.info("启动程序>>>")
    bot_service = BotService()
    bot_service.run()
    logging.info("<<<启动程序成功")
