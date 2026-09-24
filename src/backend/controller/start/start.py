from contextlib import asynccontextmanager
from src.backend.database.infra.pool import load_pool
from src.backend.database.start.creation import GenerateDatabase
from fastapi import FastAPI
from asyncmy import Pool

@asynccontextmanager
async def start(app: FastAPI):
    try:
        await GenerateDatabase().gen_all() #<--- Such instance will generate the automatically
    except Exception as e:
        print("Error during creation of the database")
        raise e
    else:
        print("database created successfully")
        pool: Pool = await load_pool()
        app.state.pool = pool #<--- Sharing the pool
        yield #<--- Running the API
        print("api finished successfully")