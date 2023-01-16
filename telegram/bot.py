from aiogram import types
from aiogram.utils.exceptions import MessageToDeleteNotFound

import pickle
from datetime import timedelta

from telegram import dp, bot
from entities.base_entity import Tamagotchi
from database.connection import async_redis, celery_app, rq
from .keyboards import needs_keyboard
from worker.redis_store import get_pet


@dp.message_handler(commands=['start'])
async def start_pet(message: types.Message):
    pet = await async_redis.get(message.from_user.id)
    if pet:
        pet = pickle.loads(pet)
    else:
        pet = Tamagotchi(message.from_user.id)
        await async_redis.set(message.from_user.id, pickle.dumps(pet))
    # rq.enqueue_in(
    #     timedelta(seconds=5),
    #     get_pet,
    #     message.from_user.id
    # )
    get_pet.delay(message.from_user.id)
    prev_message = message.message_id - 1
    try:
        await bot.delete_message(message.chat.id, prev_message)
    except MessageToDeleteNotFound:
        pass
    await message.delete()
    pet_needs = "\n".join(pet.__str__().split(" | "))
    await message.answer(f"{pet.image}\n{pet_needs}", reply_markup=needs_keyboard())

@dp.message_handler()
async def message_remove(message: types.Message):
    await message.delete()

@dp.callback_query_handler()
async def needs_callback(callback_query: types.CallbackQuery):
    pet = await async_redis.get(callback_query.from_user.id)
    pet: Tamagotchi = pickle.loads(pet)
    if pet.busy:
        bot.answer_callback_query(callback_query.id, "Pet is busy")
        return None
    if callback_query.data.lower() == "eat":
        pet.hungry -= 10
    elif callback_query.data.lower() == "sleep":
        # pet.busy = True
        pet.fatigue -= 100
    prev_message = callback_query.message.message_id
    try:
        await bot.delete_message(callback_query.from_user.id, prev_message)
    except MessageToDeleteNotFound:
        pass
    pet_needs = "\n".join(pet.__str__().split(" | "))
    await async_redis.set(callback_query.from_user.id, pickle.dumps(pet))
    await bot.send_message(
        callback_query.from_user.id, 
        f"{pet.image}\n{pet_needs}", 
        reply_markup=needs_keyboard()
    )

async def send_message():
    await bot.send_message("240641855", "Hello")
