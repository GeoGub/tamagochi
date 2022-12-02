import aioredis

async def publish(*args):
    for arg in args:
        print(arg)
    # redis = await aioredis.from_url("redis://localhost")
    # pub = redis
    # await pub.publish("channel:1", command)
    # await pub.close()

def t(*args):
    print("hello World")
