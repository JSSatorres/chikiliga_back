from pymongo import MongoClient
from bson.objectid import ObjectId
import os

class MongoDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGODB_URI"))
        self.db = self.client[os.getenv("MONGODB_DB_NAME")]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close(self):
        self.client.close()