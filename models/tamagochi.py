from sqlalchemy import Table, Column, Integer, String, Float

from database import metadata

user = Table(
    "tamagochies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True),
    Column("hp", Integer, unique=True),
    Column("hungry", Integer, unique=True),
    Column("fatigue", Integer, unique=True),
    Column("age", Integer, unique=True),
    Column("life_rate", Float, unique=True),
)
