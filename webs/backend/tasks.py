from celery.decorators import task,periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab

from .scrap import scraps


logger = get_task_logger()
@periodic_task(
    run_every=(crontab(minute='*/59')),
    name="periodic_scraping_of_dev.to",
    ignore_result=True )

def period_scraps():
    scraps()
    logger.info("Scrapped dev.to")