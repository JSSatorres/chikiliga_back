from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.settings import settings

class MongoDBConnection:
    def __init__(self):
        self.client = MongoClient(settings.mongo_uri, server_api=ServerApi('1'))
        self.db = self.client.get_default_database()
        # self.db = self.client["chikiliga"]

        # Prueba de conexión (Ping)
        try:
            self.client.admin.command('ping')
            print("¡Conexión exitosa a MongoDB!")
        except Exception as e:
            print("Error al conectar a MongoDB:", e)

    def get_database(self):
        return self.db

mongo_connection = MongoDBConnection()
