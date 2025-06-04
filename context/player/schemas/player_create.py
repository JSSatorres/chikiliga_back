from pydantic import BaseModel, Field
from typing import List


class PlayerCreate(BaseModel):
    """
    Schema for creating a new player.
    This schema defines the required and optional fields
    for player creation requests.
    """
    name: str = Field(..., description="The name of the player")
    age: int = Field(..., ge=0, description="The age of the player")
    position: str = Field(..., description="The position of the player")
    team: str = Field(..., description="The team the player belongs to")
    market_value: float = Field(default=0.0, description="Player's market value")
    points: float = Field(default=0.0, description="Player's score/points")
    free_kick_order: int = Field(default=0, description="Player's position in free kick order")
    penalty_order: int = Field(default=0, description="Player's position in penalty order")
    corner_order: int = Field(default=0, description="Player's position in corner kick order")
    last_5_games_points: List[float] = Field(default_factory=list, description="Player's points in last 5 games")
    team_last_5_games: List[str] = Field(default_factory=list, description="Team's results in last 5 games")
    team_win_percentage: float = Field(default=0.0, description="Team's win percentage")
    goals: int = Field(default=0, description="Total number of goals scored")
    assists: int = Field(default=0, description="Total number of assists")
    last_5_games_goals: int = Field(default=0, description="Goals scored in last 5 games")
    last_5_games_assists: int = Field(default=0, description="Assists made in last 5 games")