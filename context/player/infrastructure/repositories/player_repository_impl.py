from typing import List, Optional
from pymongo import MongoClient
from bson import ObjectId
from context.player.domain.player_repository import PlayerRepository
from context.player.domain.player import Player
from shared.domain.value_objects.player_id import PlayerId
from shared.core.config.settings import get_settings


class PlayerRepositoryImpl(PlayerRepository):
    """
    MongoDB implementation of the PlayerRepository interface.
    This class provides concrete implementation for player persistence
    using MongoDB as the storage backend.
    """

    def __init__(self):
        settings = get_settings()
        self.client = MongoClient(settings.MONGODB_URL)
        self.db = self.client[settings.MONGODB_DATABASE]
        self.collection = self.db['players']

    async def find_by_id(self, player_id: PlayerId) -> Optional[Player]:
        """
        Find a player by their unique identifier.
        
        Args:
            player_id: The unique identifier of the player
            
        Returns:
            The player if found, None otherwise
        """
        try:
            # Convert PlayerId to ObjectId for MongoDB query
            data = self.collection.find_one({"_id": ObjectId(player_id.value)})
            if data:
                # Convert MongoDB ObjectId to string for domain object
                data["id"] = str(data["_id"])
                del data["_id"]
                return Player.from_primitives(data)
            return None
        except Exception:
            return None

    async def save(self, player: Player) -> None:
        """
        Save a player to the repository.
        
        Args:
            player: The player entity to save
        """
        try:
            player_data = player.to_primitives()
            # Use the player ID as MongoDB _id
            object_id = ObjectId(player_data["id"])
            player_data["_id"] = object_id
            del player_data["id"]  # Remove id since we use _id
            
            self.collection.update_one(
                {"_id": object_id}, 
                {"$set": player_data}, 
                upsert=True
            )
        except Exception as e:
            raise RuntimeError(f"Failed to save player: {str(e)}")

    async def find_all(self) -> List[Player]:
        """
        Retrieve all players from the repository.
        
        Returns:
            List of all players
        """
        try:
            players = []
            for data in self.collection.find():
                # Convert MongoDB ObjectId to string for domain object
                data["id"] = str(data["_id"])
                del data["_id"]
                player = Player.from_primitives(data)
                players.append(player)
            return players
        except Exception:
            return []

    async def delete(self, player_id: PlayerId) -> bool:
        """
        Delete a player from the repository.
        
        Args:
            player_id: The unique identifier of the player to delete
            
        Returns:
            True if the player was deleted, False if not found
        """
        try:
            result = self.collection.delete_one({"_id": ObjectId(player_id.value)})
            return result.deleted_count > 0
        except Exception:
            return False

    async def exists(self, player_id: PlayerId) -> bool:
        """
        Check if a player exists in the repository.
        
        Args:
            player_id: The unique identifier of the player
            
        Returns:
            True if the player exists, False otherwise
        """
        try:
            count = self.collection.count_documents({"_id": ObjectId(player_id.value)})
            return count > 0
        except Exception:
            return False
