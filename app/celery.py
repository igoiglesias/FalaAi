from celery import Celery
import logging

from app.config.settings import settings


logging.basicConfig(level=settings.LOGGING_LEVEL)


celery = Celery(
    "app", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)  # type: ignore

celery.conf.update(
    task_serializer="json",
    broker_connection_retry_on_startup=True,
    broker_connection_retry=False,
    worker_pool="threads",
    worker_prefetch_multiplier=1,
    task_acks_late=True,
)
celery.autodiscover_tasks(["app.services.user"])
