from GetSaveNews import SaveToDb
from GetSaveNews import MzPrint
from apscheduler.schedulers.blocking  import BlockingScheduler
from datetime import datetime

# @sched.scheduled_job('interval', hours=10)
# def timed_job():
#     print('This job is run every 10 hours.')
#     SaveToDb()

# @sched.scheduled_job('cron', day_of_week='mon-fri', hour=17)
# def scheduled_job():
#     print('This job is run every weekday at 5pm.')

sched = BlockingScheduler()

#heroku web panel will shows active workers
# @sched.scheduled_job('interval', seconds=5)
# def timed_job():
#     MzPrint()

@sched.scheduled_job('interval', minutes=120)
def timed_job():
    SaveToDb()


if __name__ == '__main__':
    sched.start()