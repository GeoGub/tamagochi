from rq import Connection, Worker
import aioredis
import asyncio
from redis import Redis
from test import t

# from publisher import publish

def main():
    redis = Redis("host.docker.internal")
    a = redis.ping()
    print(a)

    with Connection(redis):
        worker = Worker('high')
        worker.work(with_scheduler=True)


if __name__ == "__main__":
    main()
