from background_task.tasks import tasks, autodiscover
from apscheduler.schedulers.background import BackgroundScheduler


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tasks.run_next_task, 'interval', seconds=60)
    scheduler.start()
