from pymongo import MongoClient
from bson import ObjectId
from context.player.domain.player_repository import PlayerRepository
from context.player.domain.player import Player

class MongoPlayerRepository(PlayerRepository):
    def __init__(self, db_url: str, db_name: str):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db['players']

    def get_by_id(self, player_id: str) -> Player:
        data = self.collection.find_one({"_id": ObjectId(player_id)})
        return Player(**data) if data else None

    def save(self, player: Player) -> Player:
        player_data = player.to_primitives()
        self.collection.update_one({"_id": player.id}, {"$set": player_data}, upsert=True)
        return player

    def get_all(self) -> list[Player]:
        return [Player(**data) for data in self.collection.find()]