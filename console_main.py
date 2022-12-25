from entities.base_entity import Tamagochi
from console.console import Console
import asyncio

from datetime import timedelta

# from database.database import rq
# from console.publisher import publish


def schedule_needs():
    fatigue = {
        "action": "s",
        "value": -10,
        "time": timedelta(seconds=10)
    }
    # age = {
    #     "action": "a",
    #     "time": timedelta(seconds=30)
    # }
    # hungry = {
    #     "action": "h",
    #     "value": -10,
    #     "time": timedelta(seconds=20)
    # }
    # rq.enqueue_in(
    #     fatigue.pop("time"),
    #     publish,
    #     action=fatigue.pop("action"),
    #     value=fatigue.pop("value")
    # )


if __name__ == "__main__":
    # schedule_needs()
    pet = Tamagochi()
    console = Console(pet)
    asyncio.run(console.run())
