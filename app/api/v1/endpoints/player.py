from fastapi import APIRouter, HTTPException
from context.player.presentation.player_controller import PlayerController
from context.player.schemas.player import PlayerCreate, PlayerResponse

router = APIRouter()
player_controller = PlayerController()

@router.post("/", response_model=PlayerResponse)
async def create_player(player: PlayerCreate):
    try:
        return await player_controller.create_player(player)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{player_id}", response_model=PlayerResponse)
async def get_player(player_id: str):
    try:
        return await player_controller.get_player(player_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[PlayerResponse])
async def get_all_players():
    try:
        return await player_controller.get_all_players()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{player_id}")
async def delete_player(player_id: str):
    try:
        await player_controller.delete_player(player_id)
        return {"detail": "Player deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))