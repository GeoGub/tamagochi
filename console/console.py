from os import system
import asyncio
import aioconsole

import json

from entities.base_entity import Tamagochi
from database.database import async_redis


class Console:

    def __init__(self, pet: Tamagochi) -> None:
        self.pet = pet
        self.commands = "s: Sleep; e: Eat;"

    def clear(self) -> None:
        system("cls || clear")

    def show_pet(self) -> None:
        print(self.pet.image)
        print(self.pet)

    def update_needs(self, need: dict):
        match need["command"]:
            case "s":
                self.pet.fatigue += need["value"]
            case "e":
                self.pet.hungry += need["value"]
        self.clear()
        self.show_pet()

    async def keyboard_listner(self) -> None:
        while True:
            command: str = await aioconsole.ainput(self.commands)
            need = {
                "command": command.lower(),
                "value": -10
            }
            self.update_needs(need)
            self.clear()
            self.show_pet()

    async def redis_listner(self) -> None:
        pubsub = async_redis.pubsub()
        await pubsub.psubscribe("channel:1")
        while True:
            message = await pubsub.get_message(ignore_subscribe_messages=True)
            if message is not None:
                need: bytes = message["data"]
                self.update_needs(json.loads(need.decode()))
            await asyncio.sleep(0.3)

    async def run(self) -> None:
        self.clear()
        self.show_pet()
        # await asyncio.gather(self.keyboard_listner())
        await asyncio.gather(self.keyboard_listner(), self.redis_listner())

if __name__ == "__main__":
    tamagochi = Tamagochi()
    console = Console(tamagochi)

