from entities.base_entity import Tamagochi
from entities.console import Console
import asyncio



if __name__ == "__main__":
    pet = Tamagochi()
    console = Console(pet)
    asyncio.run(console.run())
