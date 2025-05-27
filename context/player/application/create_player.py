from context.player.domain.player import Player
from context.player.domain.player_repository import PlayerRepository
from context.player.schemas.player_create import PlayerCreate


class CreatePlayer:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    async def execute(self, player_create: PlayerCreate) -> Player:
        """
        Create a new player.
        
        Args:
            player_create: The player creation data
            
        Returns:
            The created player entity
        """
        player = Player.create(
            name=player_create.name,
            age=player_create.age,
            position=player_create.position,
            team=player_create.team,
            market_value=player_create.market_value,
            points=player_create.points,
            free_kick_order=player_create.free_kick_order,
            penalty_order=player_create.penalty_order,
            corner_order=player_create.corner_order,
            last_5_games_points=player_create.last_5_games_points,
            team_last_5_games=player_create.team_last_5_games,
            team_win_percentage=player_create.team_win_percentage,
            goals=player_create.goals,
            assists=player_create.assists,
            last_5_games_goals=player_create.last_5_games_goals,
            last_5_games_assists=player_create.last_5_games_assists
        )
        await self.player_repository.save(player)
        return player