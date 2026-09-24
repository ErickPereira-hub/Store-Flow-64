import os
import sys
import dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
dotenv.load_dotenv(".env")
from src.backend.database.start.creation import GenerateDatabase
from fastapi import FastAPI
from src.backend.routes.routes import ROUTE_USER
from contextlib import asynccontextmanager
from src.backend.database.infra.pool import load_pool
from asyncmy import Pool
from fastapi.middleware.cors import CORSMiddleware

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

api: FastAPI = FastAPI(lifespan = start)

origins = [
    "http://127.0.0.1:5500"
        ]
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

api.include_router(ROUTE_USER)