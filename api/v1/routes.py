from fastapi import APIRouter
from context.player.presentation.player_router import get_player_router

api_router_v1 = APIRouter()

api_router_v1.include_router(
    get_player_router(),
    prefix="/players",
    tags=["players"]
)

