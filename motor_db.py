import asyncio
import os
import motor.motor_asyncio
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from dotenv import load_dotenv

load_dotenv()


client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('MONGODB_URI'))

db = client['test']