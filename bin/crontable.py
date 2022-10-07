from crontab import CronTab

# 创建cron访问
cron = CronTab(user='lizehan')

# 增加新作业
job = cron.new(command='python3 ../core/todayPrice.py 2022-09-18')

# 每一分钟执行一次
job.minute.every(1)

# 写入作业
cron.write()