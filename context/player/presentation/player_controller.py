from fastapi import APIRouter, HTTPException, Depends
from context.player.application.player_service import PlayerService
from context.player.schemas.player import PlayerCreate, PlayerResponse

router = APIRouter()

@router.post("/", response_model=PlayerResponse)
async def create_player(player: PlayerCreate, player_service: PlayerService = Depends()):
    created_player = await player_service.create_player(player)
    if not created_player:
        raise HTTPException(status_code=400, detail="Player could not be created")
    return created_player

@router.get("/{player_id}", response_model=PlayerResponse)
async def get_player(player_id: str, player_service: PlayerService = Depends()):
    player = await player_service.get_player(player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.get("/", response_model=list[PlayerResponse])
async def get_all_players(player_service: PlayerService = Depends()):
    players = await player_service.get_all_players()
    return players

@router.delete("/{player_id}")
async def delete_player(player_id: str, player_service: PlayerService = Depends()):
    success = await player_service.delete_player(player_id)
    if not success:
        raise HTTPException(status_code=404, detail="Player not found")
    return {"detail": "Player deleted successfully"}