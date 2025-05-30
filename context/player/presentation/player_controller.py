from typing import List
from fastapi import APIRouter, HTTPException, status

from context.player.schemas.player_create import PlayerCreate
from context.player.schemas.player_response import PlayerResponse
from context.player.application.create_player import CreatePlayer
from context.player.application.get_player import GetPlayer
from context.player.application.get_all_players import GetAllPlayers
from context.player.application.delete_player import DeletePlayer


class PlayerController:
    
    def __init__(
        self,
        create_player_use_case: CreatePlayer,
        get_player_use_case: GetPlayer,
        get_all_players_use_case: GetAllPlayers,
        delete_player_use_case: DeletePlayer
    ):
        self.create_player_use_case = create_player_use_case
        self.get_player_use_case = get_player_use_case
        self.get_all_players_use_case = get_all_players_use_case
        self.delete_player_use_case = delete_player_use_case
        
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self):
        """Register all player-related routes with their corresponding handlers."""
        self.router.post("/", response_model=PlayerResponse)(self.create_player)
        self.router.get("/{player_id}", response_model=PlayerResponse)(self.get_player)
        self.router.get("/", response_model=List[PlayerResponse])(self.get_all_players)
        self.router.delete("/{player_id}")(self.delete_player)

    async def create_player(self, player: PlayerCreate) -> PlayerResponse:
        try:
            created_player = await self.create_player_use_case.execute(player)
            return PlayerResponse.model_validate(created_player)
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def get_player(self, player_id: str) -> PlayerResponse:
        try:
            player = await self.get_player_use_case.execute(player_id)
            return PlayerResponse.model_validate(player)
        except HTTPException:
            # Re-raise HTTP exceptions from use case
            raise
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def get_all_players(self) -> List[PlayerResponse]:
        try:
            players = await self.get_all_players_use_case.execute()
            return [PlayerResponse.model_validate(player) for player in players]
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def delete_player(self, player_id: str) -> dict:
        try:
            return await self.delete_player_use_case.execute(player_id)
        except HTTPException:
            # Re-raise HTTP exceptions from use case
            raise
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) 