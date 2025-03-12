from typing import Any
from context.player.domain.player import Player
from context.player.domain.player_repository import PlayerRepository
from context.player.schemas.player_create import PlayerCreate

class CreatePlayer:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    async def execute(self, player_create: PlayerCreate) -> Player:
        player = Player.create(
            name=player_create.name,
            age=player_create.age,
            position=player_create.position,
            team=player_create.team
        )
        return await self.player_repository.save(player)