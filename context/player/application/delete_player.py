from fastapi import HTTPException, status
from context.player.domain.player_repository import PlayerRepository
from shared.domain.value_objects.player_id import PlayerId


class DeletePlayer:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    async def execute(self, player_id: str) -> dict:
        """
        Delete a player by their unique identifier.
        
        Args:
            player_id: The string representation of the player ID
            
        Returns:
            Success message dictionary
            
        Raises:
            HTTPException: If the player is not found
        """
        player_id_vo = PlayerId(player_id)
        success = await self.player_repository.delete(player_id_vo)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Player with ID {player_id} not found"
            )
        
        return {"detail": "Player deleted successfully"}