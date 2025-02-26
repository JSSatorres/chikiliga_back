from pymongo import MongoClient
from bson import ObjectId
from backend.context.player.domain.player_repository import PlayerRepository
from backend.context.player.domain.player import Player

class MongoPlayerRepository(PlayerRepository):
    def __init__(self, db_url: str, db_name: str):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db['players']

    def get_by_id(self, player_id: str):
        data = self.collection.find_one({"id": player_id})
        return Player(**data) if data else None

    def save(self, player: Player):
        self.collection.update_one({"id": player.id.value}, {"$set": player.to_dict()}, upsert=True)
        return player

    def get_all(self):
        return [Player(**data) for data in self.collection.find()]
        
        