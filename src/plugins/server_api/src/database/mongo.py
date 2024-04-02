from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import asyncio

class MongoManager:
    def __init__(self):
        self.uri = "mongodb://localhost:27017"
        self.client = AsyncIOMotorClient(self.uri, server_api=ServerApi('1'))
        
    def __create_database(self):
        self.db = self.client['boards']
    
    def __create_collection(self):
        self.collection = self.db['board_one']
    
    async def ping_server(self):
        self.__create_database()
        self.__create_collection()
        doc = {'id': 'qwe'}
        await self.db.board_one.insert_one(doc)
        try:
            await self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
      
asyncio.run(MongoManager().ping_server())