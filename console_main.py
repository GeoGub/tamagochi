from entities.base_entity import Tamagotchi
from console.console import Console
import asyncio


if __name__ == "__main__":
    pet = Tamagotchi()
    console = Console(pet)
    asyncio.run(console.run())
