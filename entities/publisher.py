import aioredis

async def publish(command: str):
    redis = await aioredis.from_url("redis://localhost")
    pub = redis
    await pub.publish("channel:1", command)
    await pub.close()
