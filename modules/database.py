from os import getenv
from loguru import logger
from dotenv import load_dotenv
from mongoengine import connect

load_dotenv()
DB_NAME = getenv("DB_NAME")
MONGO_CONNECTION_STRING = getenv("MONGO_CONNECTION_STRING")

MONGODB_SETTINGS = {"db": DB_NAME, "host": MONGO_CONNECTION_STRING}


def connect_to_mongo():
    connect(**MONGODB_SETTINGS)
    logger.info("Connected to MongoDB")
