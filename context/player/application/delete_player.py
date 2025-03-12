from fastapi import HTTPException, status
from context.player.domain.player_repository import PlayerRepository
from context.player.domain.value_objects.player_id import PlayerId

async def delete_player(player_id: str, player_repository: PlayerRepository):
    player_id_value = PlayerId(player_id)
    success = await player_repository.delete(player_id_value)
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Player not found"
        )
    
    return {"detail": "Player deleted successfully"}