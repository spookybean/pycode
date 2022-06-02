import asyncio
import os
import motor.motor_asyncio
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from dotenv import load_dotenv

load_dotenv()


client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv('MONGODB_URI'))

db = client['test']


async def example():
    try:
        document = await db.user.find_one({}, {'_id': 0})
    except ServerSelectionTimeoutError as e:
        print('db connection failed')
    else:
        print(document)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(example())