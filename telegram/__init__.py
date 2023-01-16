from aiogram import Bot, Dispatcher

from config import get_settings

bot = Bot(token=get_settings().telegram_api_key)
dp = Dispatcher(bot)