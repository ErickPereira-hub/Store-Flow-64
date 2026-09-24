import os
import sys
import dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
dotenv.load_dotenv(".env")
from fastapi import FastAPI
from src.backend.routes.routes import ROUTE_USER
from fastapi.middleware.cors import CORSMiddleware
from src.backend.infra.cors import origins
from src.backend.controller.start.start import start

api: FastAPI = FastAPI(lifespan = start)

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

api.include_router(ROUTE_USER)