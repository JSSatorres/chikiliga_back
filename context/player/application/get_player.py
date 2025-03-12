from typing import Optional
from fastapi import HTTPException, status
from context.player.domain.player_repository import PlayerRepository
from context.player.domain.player import Player
from context.player.schemas.player_response import PlayerResponse

async def get_player(player_id: str, player_repository: PlayerRepository) -> PlayerResponse:
    player: Optional[Player] = await player_repository.get_by_id(player_id)
    if not player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
    return PlayerResponse.from_orm(player)