from typing import Any, List
from shared.domain.aggregate_root import AggregateRoot
from shared.domain.value_objects.player_id import PlayerId


class Player(AggregateRoot):
    def __init__(
        self, 
        id: PlayerId, 
        name: str, 
        age: int,
        position: str, 
        team: str, 
        market_value: float = 0.0,
        points: float = 0.0,
        free_kick_order: int = 0,
        penalty_order: int = 0,
        corner_order: int = 0,
        last_5_games_points: List[float] = None,
        team_last_5_games: List[str] = None,
        team_win_percentage: float = 0.0,
        goals: int = 0,
        assists: int = 0,
        last_5_games_goals: int = 0,
        last_5_games_assists: int = 0
    ):
        self.id = id
        self.name = name
        self.age = age
        self.position = position
        self.team = team
        self.market_value = market_value
        self.points = points
        self.free_kick_order = free_kick_order
        self.penalty_order = penalty_order
        self.corner_order = corner_order
        self.last_5_games_points = last_5_games_points or []
        self.team_last_5_games = team_last_5_games or []
        self.team_win_percentage = team_win_percentage
        self.goals = goals
        self.assists = assists
        self.last_5_games_goals = last_5_games_goals
        self.last_5_games_assists = last_5_games_assists

    @classmethod
    def create(
        cls, 
        name: str, 
        age: int,
        position: str, 
        team: str,
        market_value: float = 0.0,
        points: float = 0.0,
        free_kick_order: int = 0,
        penalty_order: int = 0,
        corner_order: int = 0,
        last_5_games_points: List[float] = None,
        team_last_5_games: List[str] = None,
        team_win_percentage: float = 0.0,
        goals: int = 0,
        assists: int = 0,
        last_5_games_goals: int = 0,
        last_5_games_assists: int = 0
    ) -> 'Player':
        """Create a new player with auto-generated ID."""
        import uuid
        player_id = PlayerId(str(uuid.uuid4()))
        
        return cls(
            id=player_id,
            name=name,
            age=age,
            position=position,
            team=team,
            market_value=market_value,
            points=points,
            free_kick_order=free_kick_order,
            penalty_order=penalty_order,
            corner_order=corner_order,
            last_5_games_points=last_5_games_points,
            team_last_5_games=team_last_5_games,
            team_win_percentage=team_win_percentage,
            goals=goals,
            assists=assists,
            last_5_games_goals=last_5_games_goals,
            last_5_games_assists=last_5_games_assists
        )

    def to_primitives(self) -> dict[str, Any]:
        return {
            "id": self.id.value,
            "name": self.name,
            "age": self.age,
            "position": self.position,
            "team": self.team,
            "market_value": self.market_value,
            "points": self.points,
            "free_kick_order": self.free_kick_order,
            "penalty_order": self.penalty_order,
            "corner_order": self.corner_order,
            "last_5_games_points": self.last_5_games_points,
            "team_last_5_games": self.team_last_5_games,
            "team_win_percentage": self.team_win_percentage,
            "goals": self.goals,
            "assists": self.assists,
            "last_5_games_goals": self.last_5_games_goals,
            "last_5_games_assists": self.last_5_games_assists
        }

    @classmethod
    def from_primitives(cls, plain_data: dict[str, Any]) -> 'Player':
        return cls(
            id=PlayerId(plain_data["id"]),
            name=plain_data["name"],
            age=plain_data["age"],
            position=plain_data["position"],
            team=plain_data["team"],
            market_value=plain_data.get("market_value", 0.0),
            points=plain_data.get("points", 0.0),
            free_kick_order=plain_data.get("free_kick_order", 0),
            penalty_order=plain_data.get("penalty_order", 0),
            corner_order=plain_data.get("corner_order", 0),
            last_5_games_points=plain_data.get("last_5_games_points", []),
            team_last_5_games=plain_data.get("team_last_5_games", []),
            team_win_percentage=plain_data.get("team_win_percentage", 0.0),
            goals=plain_data.get("goals", 0),
            assists=plain_data.get("assists", 0),
            last_5_games_goals=plain_data.get("last_5_games_goals", 0),
            last_5_games_assists=plain_data.get("last_5_games_assists", 0)
        )