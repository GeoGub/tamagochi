import databases
import sqlalchemy
import aioredis
from redis import Redis
from celery import Celery
from rq import Queue

from config import get_settings

# database = databases.Database(get_settings().database_url)
metadata = sqlalchemy.MetaData()
async_redis = aioredis.from_url(
    url=get_settings().redis_host #! refactor this
)

redis = Redis(host="localhost", password=get_settings().redis_password)
celery_app = Celery("tasks", broker="redis://localhost")
rq = Queue("high", connection=redis)
