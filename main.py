# coding=utf-8
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tgbot.jobs.table_job import TableJob
from tgbot.service.bot_service import BotService

if __name__ == '__main__':
    logging.info("启动程序>>>")
    scheduler = AsyncIOScheduler(timezone='Asia/Shanghai')
    scheduler.add_job(func=TableJob().run, trigger="interval", seconds=120)
    scheduler.start()

    bot_service = BotService()
    bot_service.run()
    logging.info("<<<启动程序成功")
