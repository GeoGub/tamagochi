import pickle
import asyncio
from celery import Task
from aiogram.types import Message

from database.connection import celery_app, redis
from entities.base_entity import Tamagotchi
from telegram import bot
from telegram.keyboards import needs_keyboard

def redis_get_message_send(func):
    def wrapper(self: Task, user_id):
        pet: Tamagotchi = pickle.loads(redis.hget(user_id, "pet"))
        last_message_id: str = redis.hget(user_id, "last_message_id")
        pet = func(self, user_id, pet)
        pet_needs = "\n".join(pet.__str__().split(" | "))
        loop = asyncio.get_event_loop()
        delete_message_corutin = bot.delete_message(user_id, last_message_id)
        send_message_corutin = bot.send_message(
            user_id, 
            f"{pet.image}\n{pet_needs}", 
            reply_markup=needs_keyboard()
        )
        loop.run_until_complete(delete_message_corutin)
        last_message: Message = loop.run_until_complete(send_message_corutin)
        redis.hset(user_id, "pet", pickle.dumps(pet))
        redis.hset(user_id, "last_message_id", last_message.message_id)
    return wrapper

@celery_app.task(bind=True)
@redis_get_message_send
def reduce_hungry(self: Task, user_id: str, pet: Tamagotchi) -> Tamagotchi:
    pet.hungry += 10
    self.apply_async((user_id, ), countdown=15)
    return pet

@celery_app.task(bind=True)
@redis_get_message_send
def reduce_fatigue(self: Task, user_id: str, pet: Tamagotchi) -> Tamagotchi:
    pet.fatigue += 15
    self.apply_async((user_id, ), countdown=5)
    return pet
