from rq import Connection, Worker, Queue
import aioredis
import asyncio
from redis import Redis

from datetime import timedelta, datetime

from publisher import publish

def main():
    redis = Redis("localhost")
    rq = Queue("high", connection=redis)
    rq.enqueue_at(
        datetime.now()+timedelta(seconds=3),
        publish,
        "hello"
    )
    with Connection(redis):
        worker = Worker('high')
        worker.work(with_scheduler=True)


if __name__ == "__main__":
    main()
