from os import system
import asyncio
import aioconsole

import json
import time

from entities.base_entity import Tamagochi
from database.database import async_redis


class Console:

    def __init__(self, pet: Tamagochi) -> None:
        self.pet = pet
        self.commands = "s: Sleep; e: Eat;"

    def show_pet(self) -> None:
        system("cls || clear")
        print(self.pet.image)
        print(self.pet)
        print(self.commands)

    async def update_needs(self, need: dict):
        self.show_pet()
        if self.pet.busy is True:
            return
        match need["command"]:
            case "s":
                self.pet.busy = True
                await asyncio.sleep(20)
                self.pet.fatigue -= need["value"]
                self.pet.busy = False
            case "e":
                self.pet.hungry -= need["value"]
        self.show_pet()

    async def keyboard_listner(self) -> None:
        while True:
            command: str = await aioconsole.ainput()
            need = {
                "command": command
            }
            match command:
                case "s":
                    need["value"] = 100
                case "e":
                    need["value"] = 15

            await self.update_needs(need)
            self.show_pet()
    
    async def fatigue_listner(self) -> None:
        while True:
            await asyncio.sleep(self.pet.timedelta_fatigue)
            if self.pet.busy:
                continue
            self.pet.fatigue += 5
            self.show_pet()

    async def hungry_listner(self) -> None:
        while True:
            await asyncio.sleep(self.pet.timedelta_hungry)
            if self.pet.busy:
                continue
            self.pet.hungry += 5
            self.show_pet()

    async def regeniration_listner(self) -> None:
        while True:
            await asyncio.sleep(self.pet.timedelta_regeniration)
            if self.pet.hungry != 100 and self.pet.fatigue != 100:
                self.pet.hp += 2
                self.show_pet()

    async def run(self) -> None:
        self.show_pet()
        await asyncio.gather(
            self.keyboard_listner(), 
            self.fatigue_listner(), 
            self.hungry_listner(),
            self.regeniration_listner()
        )

if __name__ == "__main__":
    tamagochi = Tamagochi()
    console = Console(tamagochi)

