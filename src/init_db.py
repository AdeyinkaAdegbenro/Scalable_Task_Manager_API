import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from flask import g
from redis import Redis

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"), echo=True)

def get_db():
    session = Session(engine)
    return session

def get_redis():
    return Redis(
        host='redis', port=6379, decode_responses=True
    )