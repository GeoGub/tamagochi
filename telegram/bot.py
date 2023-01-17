from aiogram import types
from aiogram.utils.exceptions import MessageToDeleteNotFound
from aioredis.exceptions import ResponseError

import pickle
from datetime import timedelta

from telegram import dp, bot
from entities.base_entity import Tamagotchi
from database.connection import async_redis
from .keyboards import needs_keyboard
from worker.redis_store import reduce_hungry, reduce_fatigue


@dp.message_handler(commands=['start'])
async def start_pet(message: types.Message):
    pet = await async_redis.hget(message.from_user.id, "pet")
    if pet:
        pet = pickle.loads(pet)
    else:
        pet = Tamagotchi(message.from_user.id)
        await async_redis.hset(message.from_user.id, "pet", pickle.dumps(pet))
    #! Add one tab   
    # get_pet.apply_async((message.from_user.id, ), countdown=5)
    reduce_hungry.apply_async((message.from_user.id, ), countdown=1)
    # reduce_fatigue.apply_async((message.from_user.id, ), countdown=10)
    prev_message = message.message_id - 1
    try:
        await bot.delete_message(message.chat.id, prev_message)
    except MessageToDeleteNotFound:
        pass
    await message.delete()
    pet_needs = "\n".join(pet.__str__().split(" | "))
    last_message = await message.answer(
        f"{pet.image}\n{pet_needs}", 
        reply_markup=needs_keyboard()
    )
    await async_redis.hset(
        message.from_user.id, 
        "last_message_id", 
        last_message.message_id
    )

@dp.message_handler()
async def message_remove(message: types.Message):
    await message.delete()

@dp.callback_query_handler()
async def needs_callback(callback_query: types.CallbackQuery):
    pet = await async_redis.hget(callback_query.from_user.id, "pet")
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
    await async_redis.hset(callback_query.from_user.id, "pet", pickle.dumps(pet))
    last_message = await bot.send_message(
        callback_query.from_user.id, 
        f"{pet.image}\n{pet_needs}", 
        reply_markup=needs_keyboard()
    )
    await async_redis.hset(
        callback_query.from_user.id, 
        "last_message_id", 
        last_message.message_id
    )

async def send_message():
    await bot.send_message("240641855", "Hello")
