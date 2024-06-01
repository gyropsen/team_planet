import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore

from django.conf import settings

from miner.models import Info
from users.models import User

logger = logging.getLogger(__name__)
scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)


def get_points(user_info):
    print(user_info, "get_points", user_info.per_second)
    user_info.amount += user_info.per_second
    user_info.save()
    logger.info(f"get_points {user_info.pk} done!")


def check_jobs():
    """
    Проверка каждого пользователя на наличие информации,
    если информация есть - пропуск, нет - добавление периодической задачи
    """
    print("check_jobs")
    scheduler.print_jobs()
    for user in User.objects.filter(is_active=True):
        print(user, User.objects.all())
        if not Info.objects.filter(user=user).exists():
            # Информации нет, добавляем периодическую задачу, создаем информацию о юзере
            user_info = Info.objects.create(
                user=user,
                amount=0,
                per_second=1
            )
            user_info.save()

            scheduler.add_job(
                get_points,
                trigger=CronTrigger(second=f"*/1"),
                id=f"get_points {user_info.pk}",
                max_instances=1,
                args=[user_info],
                replace_existing=True,
            )
        print(user, Info.objects.filter(user=user))
    logger.info("check_jobs done!")


def start_scheduler():
    """
    Добавление задания проверки рассылок
    """
    scheduler.add_jobstore(DjangoJobStore(), "default")

    scheduler.add_job(
        check_jobs,
        trigger=CronTrigger(second="*/10"),
        id="check_jobs",
        max_instances=1,
        replace_existing=True,
    )
    logger.info("Added job 'check_jobs'.")

    try:
        logger.info("Starting scheduler...")
        scheduler.start()
    except KeyboardInterrupt:
        logger.info("Stopping scheduler...")
        scheduler.shutdown()
        logger.info("Scheduler shut down successfully!")
