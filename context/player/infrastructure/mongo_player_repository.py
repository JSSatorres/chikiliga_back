from typing import List, Optional
from pymongo import MongoClient
from bson import ObjectId
from context.player.domain.player_repository import PlayerRepository
from context.player.domain.player import Player
from shared.domain.value_objects.player_id import PlayerId

class MongoPlayerRepository(PlayerRepository):
    def __init__(self, db_url: str, db_name: str):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db['players']

    async def find_by_id(self, player_id: PlayerId) -> Optional[Player]:

        try:
            data = self.collection.find_one({"_id": ObjectId(player_id.value)})
            if data:
                # Convertir el ObjectId de MongoDB a string para el value object
                data["id"] = str(data["_id"])
                del data["_id"]
                return Player.from_primitives(data)
            return None
        except Exception:
            return None

    async def save(self, player: Player) -> bool:
        try:
            player_data = player.to_primitives()
            # Usar el ID del player como _id de MongoDB
            object_id = ObjectId(player_data["id"])
            player_data["_id"] = object_id
            del player_data["id"]  # Remover el id ya que usamos _id
            
            result = self.collection.update_one(
                {"_id": object_id}, 
                {"$set": player_data}, 
                upsert=True
            )
            return result.acknowledged
        except Exception:
            return False

    async def find_all(self) -> List[Player]:
        try:
            players = []
            for data in self.collection.find():
                # Convertir el ObjectId de MongoDB a string para el value object
                data["id"] = str(data["_id"])
                del data["_id"]
                player = Player.from_primitives(data)
                players.append(player)
            return players
        except Exception:
            return []

    async def delete(self, player_id: PlayerId) -> bool:
        try:
            result = self.collection.delete_one({"_id": ObjectId(player_id.value)})
            return result.deleted_count > 0
        except Exception:
            return False

    async def exists(self, player_id: PlayerId) -> bool:
        try:
            count = self.collection.count_documents({"_id": ObjectId(player_id.value)})
            return count > 0
        except Exception:
            return False