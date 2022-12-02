from os import system
import asyncio
import aioconsole
import aioredis
from rq import Queue
import json

import random
from datetime import datetime, timedelta

from base_entity import Tamagochi
from publisher import publish


class Console:

    def __init__(self, pet: Tamagochi) -> None:
        self.pet = pet
        self.fatigue = {
            "action": "s",
            "value": -10,
            "time": timedelta(seconds=10)
        }
        self.age = {
            "action": "a",
            "time": timedelta(seconds=30)
        }
        self.hungry = {
            "action": "h",
            "value": -10,
            "time": timedelta(seconds=20)
        }


    def clear(self) -> None:
        system("cls || clear")

    def show_pet(self) -> None:
        print(self.pet.image)
        print(self.pet)

    def check_command(self, command: str, value: int | float) -> None:
        match command.lower():
            case "e":
                self.pet.update_hungry(value)
            case "s":
                self.pet.update_fatigue(value)
            case _:
                return None
        return None

    async def keyboard_listner(self) -> None:
        while True:
            command = await aioconsole.ainput(
                "s: Sleep; "\
                "e: Eat; "
            )
            self.check_command(command, -10)
            self.clear()
            self.show_pet()
            
    # Доделать redis listner
    async def redis_listner(self) -> None:
        pubsub = self.redis.pubsub()
        await pubsub.psubscribe("channel:1")
        while True:
            message = await pubsub.get_message(ignore_subscribe_messages=True)
            if message is not None:
                self.check_command(message)
            else:
                print("wait")
            await asyncio.sleep(1)

    async def run(self) -> None:
        self.async_redis = await aioredis.from_url("redis://localhost")
        self.rq = Queue("high", connection=self.async_redis)
        self.rq.enqueue_in(
            self.fatigue["time"],
            publish,
            self.fatigue["action"],
            self.fatigue["value"]
        )
        self.clear()
        self.show_pet()
        await asyncio.gather(self.keyboard_listner(), self.redis_listner())

