from fastapi import APIRouter
from backend.context.player.presentation.player_router import get_player_router


api_router_v1 = APIRouter()

api_router_v1.include_router(
    get_player_router(),
    prefix="/players",
    tags=["players"]
)

# Add other routers when available
# api_router_v1.include_router(
#     get_team_router(),
#     prefix="/teams",
#     tags=["teams"]
# )