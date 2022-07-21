```shell
pip install -r requirements.txt
```

apscheduler 定時調度舉例

### cron 模式

```python
scheduler.add_job(job_func, 'cron', month='1-3,7-9', day='0, tue', hour='0-3')

# 表示2017年3月22日17时19分07秒执行该程序
sched.add_job(my_job, 'cron', year=2017, month=3, day=22, hour=17, minute=19, second=7)

# 表示任务在6,7,8,11,12月份的第三个星期五的00:00,01:00,02:00,03:00 执行该程序
sched.add_job(my_job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')

# 表示从星期一到星期五5:30（AM）直到2014-05-30 00:00:00
sched.add_job(my_job(), 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2014-05-30')

# 表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
sched.add_job(my_job, 'cron', second='*/5')
```

### interval 模式

```python
log.info('>>>>> 启动检测 pod 存活 任务  <<<<<')
scheduler.add_job(func=DetectPodHealthJob().run, trigger="interval", seconds=10)

log.info('>>>>> 启动拉取启动 x个 pod 列表 任务  <<<<<')
scheduler.add_job(func=RunPodJob().run, trigger="interval", seconds=3)

log.info('>>>>> 启动拉取 关闭x个 pod 列表 任务  <<<<<')
scheduler.add_job(func=StopPodJob().run, trigger="interval", seconds=1800)

log.info('>>>>> 启动补偿推送启动的新 pod 任务  <<<<<')
scheduler.add_job(func=PushNewPodJob().run, trigger="interval", seconds=10)

log.info('>>>>> 启动清理数据 任务  <<<<<')
scheduler.add_job(func=ClearPodDataJob().run, trigger="interval", seconds=24 * 3600)
```
