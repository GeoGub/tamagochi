from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def needs_keyboard():
    eat_btn = InlineKeyboardButton("Eat", callback_data="eat")
    sleep_btn = InlineKeyboardButton("Sleep", callback_data="sleep")
    keyboard = InlineKeyboardMarkup().add(eat_btn, sleep_btn)
    return keyboard
