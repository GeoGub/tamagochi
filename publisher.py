import aioredis
import asyncio

import json

async def publish(command: str):
    redis = await aioredis.from_url("redis://localhost")
    pub = redis
    for i in range(10):
        await pub.publish("channel:1", command)
    await pub.close()


a = {
    "command": "s",
    "value": 10
}

asyncio.run(publish(json.dumps(a)))
