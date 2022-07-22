# coding=utf-8
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tgbot.jobs.table_job import TableJob
from tgbot.service.bot_service import BotService
from tgbot.service.user_service import UserService

if __name__ == '__main__':
    logging.info("启动程序>>>")
    user_service = UserService()
    user_service.get_all()

    scheduler = AsyncIOScheduler(timezone='Asia/Shanghai')
    # 每2分鐘
    scheduler.add_job(TableJob().run, "cron", minute='*/2')
    scheduler.start()

    bot_service = BotService()
    bot_service.run()
    logging.info("<<<启动程序成功")
