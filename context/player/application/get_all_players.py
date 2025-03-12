from typing import List
from context.player.domain.player_repository import PlayerRepository
from context.player.domain.player import Player

class GetAllPlayers:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    async def execute(self) -> List[Player]:
        return await self.player_repository.get_all()