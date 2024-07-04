from fastapi import FastAPI
from .db import create_keyspace_and_tables
from .routes import router
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# create_keyspace_and_tables()

app.include_router(router)
