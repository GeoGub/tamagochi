from aiogram import executor
import asyncio

from telegram import *
from telegram.bot import *


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
    # asyncio.get_event_loop().run_until_complete(send_message())
    # asyncio.run(send_message())
