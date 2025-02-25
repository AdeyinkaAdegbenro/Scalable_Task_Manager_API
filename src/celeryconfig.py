from celery.schedules import crontab

broker_url="redis://redis:6379/0"
result_backend="redis://redis"
task_ignore_result = True
beat_schedule = {
    "notify-about-overdue-tasks": {
        "task": "task.send_overdue_task_reminder",
        "schedule": crontab(minute='*/3'),
    }
}