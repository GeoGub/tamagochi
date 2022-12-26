import databases
import sqlalchemy
import aioredis
from redis import Redis
from rq import Queue

from config import get_settings

# database = databases.Database(get_settings().database_url)
metadata = sqlalchemy.MetaData()
async_redis = aioredis.from_url(get_settings().redis_host,
                         port=get_settings().redis_port,
                         db=get_settings().redis_db, 
                         password=get_settings().redis_password)

redis = Redis(host="localhost", password=get_settings().redis_password)
rq = Queue("high", connection=redis)
