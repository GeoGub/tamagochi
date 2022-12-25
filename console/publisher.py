import aioredis

import json

async def publish(need: str):
    pub = await aioredis.from_url("redis://localhost")
    await pub.publish("channel:1", need)
    await pub.close()


if __name__ == "__main__":
    import asyncio
    need = {
        "command": "e",
        "value": -10
    }
    asyncio.run(publish(json.dumps(need)))
