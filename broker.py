from datetime import timedelta
from redis import Redis
import asyncio
from rq import Queue

from test import t

def main():
    fatigue = {
    "action": "s",
    "value": -10,
    "time": timedelta(seconds=1)
    }
    redis = Redis(host="127.0.0.1", db=0)
    rq = Queue("high", connection=redis, is_async=True)
    rq.enqueue_in(
        fatigue["time"],
        t
    )

if __name__ == "__main__":
    main()