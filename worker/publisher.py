from rq import Queue
from rq.job import get_current_job, Job
import aioredis
import asyncio
from redis import Redis

from datetime import timedelta, datetime
import json

async def publish(need: str):
    job: Job = get_current_job()
    print(job)
    print(job.enqueued_at)
    print(job.enqueued_at - job.started_at)
    # redis = Redis("localhost")
    # rq = Queue("high", connection=redis)
    # rq.enqueue_in(
    #     timedelta(seconds=5),
    #     publish,
    #     "hello"
    # )
    # pub = await aioredis.from_url("redis://localhost")
    # await pub.publish("channel:1", need)
    # await pub.close()


if __name__ == "__main__":
    import asyncio
    need = {
        "command": "e",
        "value": -10
    }
    asyncio.run(publish(json.dumps(need)))
