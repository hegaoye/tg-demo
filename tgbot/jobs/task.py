from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tgbot.jobs.table_job import TableJob

scheduler = AsyncIOScheduler(timezone='Asia/Shanghai')

# 每2分鐘
# scheduler.add_job(TableJob().run, CronTrigger.from_crontab('*/2 * * * *'))
scheduler.add_job(TableJob().run, "cron", minute='*/2')
scheduler.start()
