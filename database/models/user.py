from database.database import metadata

from sqlalchemy import Table, Column, Integer, String

user = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("chat_id", String, unique=True)
)

# user_columns = {
#     "id": user.c.id,
#     "username": user.c.username,
#     "password": user.c.password,
#     "email": user.c.email,
# }

