import pickle

from database.connection import celery_app, redis
from entities.base_entity import Tamagotchi

@celery_app.task
def get_pet(user_id):
    print("hello")
    pet = redis.get(user_id)
    print(pet)  
    pet = pickle.loads(pet)
    print(pet)

@celery_app.task
def transporter():
    pass
