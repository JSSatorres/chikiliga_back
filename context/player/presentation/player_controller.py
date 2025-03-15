import context.player.infrastructure.services.player_scraping_service as player_scraping_service
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status

from context.player.schemas.player_create import PlayerCreate
from context.player.schemas.player_response import PlayerResponse

class PlayerController:
    # def __init__(self, player_service: player_scraping_service):
    def __init__(self ):
        # self.player_service = player_service
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self):
        self.router.post("/", response_model=PlayerResponse)(self.create_player)
        self.router.get("/{player_id}", response_model=PlayerResponse)(self.get_player)
        self.router.get("/", response_model=list[PlayerResponse])(self.get_all_players)
        self.router.delete("/{player_id}")(self.delete_player)

    async def create_player(self, player: PlayerCreate):
        try:
            created_player = await self.player_service.create_player(player)
            if not created_player:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Player could not be created")
            return created_player
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def get_player(self, player_id: str):
        try:
            player = await self.player_service.get_player(player_id)
            if not player:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
            return player
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def get_all_players(self):
        try:
            players = await self.player_service.get_all_players()
            return players
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def delete_player(self, player_id: str):
        try:
            success = await self.player_service.delete_player(player_id)
            if not success:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Player not found")
        except HTTPException as e:
            raise e 