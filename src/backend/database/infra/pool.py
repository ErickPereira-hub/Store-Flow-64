import asyncmy
from asyncmy import Pool
import os

async def load_pool() -> Pool:
    return await asyncmy.create_pool(
        minsize = 5,
        maxsize = 50,
        host = "localhost",
        user = "root",
        password = os.getenv("MYSQL_PASSWORD"),
        db = os.getenv("DB_NAME")
    )