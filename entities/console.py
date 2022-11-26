from os import system
import asyncio
import aioconsole

import random

from .base_entity import Tamagochi


class Console:

    def __init__(self, pet: Tamagochi) -> None:
        self.pet = pet

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
            self.check_command(command)
            self.clear()
            self.show_pet()
            

    async def redis_listner(self) -> None:
        while True:
            # print("listen reids")
            await asyncio.sleep(1)

    def run(self) -> None:
        ioloop = asyncio.get_event_loop()
        tasks = [
                ioloop.create_task(self.keyboard_listner()), 
                ioloop.create_task(self.redis_listner())
            ]
        wait_tasks = asyncio.wait(tasks)
        while True:
            self.clear()
            self.show_pet()
            self.keyboard_listner()
            ioloop.run_until_complete(wait_tasks)
            input()
