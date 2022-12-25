import aioredis

async def create_task(**kwargs):
    # redis = await aioredis.from_url("redis://host.docker.internal")
    print(kwargs)
    # pub = redis
    # await pub.publish("channel:1", "command")
    # await pub.close()
