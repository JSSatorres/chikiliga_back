from pydantic import BaseModel, Field
from typing import List

class PlayerCreate(BaseModel):
    name: str = Field(..., description="The name of the player")
    age: int = Field(..., ge=0, description="The age of the player")
    position: str = Field(..., description="The position of the player")
    team_id: str = Field(..., description="The ID of the team the player belongs to")
    points: float = Field(..., description="Player's score/points")
    free_kick_order: int = Field(..., description="Player's position in free kick order")
    penalty_order: int = Field(..., description="Player's position in penalty order")
    corner_order: int = Field(..., description="Player's position in corner kick order")
    last_5_games_points: List[float] = Field(..., description="Player's points in last 5 games")
    team_last_5_games: List[str] = Field(..., description="Team's results in last 5 games")
    team_win_percentage: float = Field(..., description="Team's win percentage")
    goals: int = Field(..., description="Total number of goals scored")
    assists: int = Field(..., description="Total number of assists")
    last_5_games_goals: List[int] = Field(..., description="Goals scored in last 5 games")
    last_5_games_assists: List[int] = Field(..., description="Assists made in last 5 games")