from typing import Optional
from fastapi import HTTPException, status
from context.player.domain.player_repository import PlayerRepository
from context.player.domain.player import Player
from shared.domain.value_objects.player_id import PlayerId


class GetPlayer:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    async def execute(self, player_id: str) -> Player:
        """
        Retrieve a player by their unique identifier.
        
        Args:
            player_id: The string representation of the player ID
            
        Returns:
            The player entity
            
        Raises:
            HTTPException: If the player is not found
        """
        player_id_vo = PlayerId(player_id)
        player: Optional[Player] = await self.player_repository.find_by_id(player_id_vo)
        
        if not player:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f"Player with ID {player_id} not found"
            )
        
        return player