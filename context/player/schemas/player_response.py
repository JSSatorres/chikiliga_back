from pydantic import BaseModel
from typing import List

class PlayerResponse(BaseModel):
    id: str
    name: str
    age: int
    position: str
    team: str
    market_value: float
    points: float
    free_kick_order: int
    penalty_order: int
    corner_order: int
    last_5_games_points: List[float]
    team_last_5_games: List[str]
    team_win_percentage: float
    goals: int
    assists: int
    last_5_games_goals: int
    last_5_games_assists: int

    class Config:
        orm_mode = True

class PlayerListResponse(BaseModel):
    players: List[PlayerResponse]

class PlayerResponse(BaseModel):
    id: str
    name: str
    age: int
    position: str
    team: str
    market_value: float
    points: float
    free_kick_order: int
    penalty_order: int
    corner_order: int
    last_5_games_points: List[float]
    team_last_5_games: List[str]
    team_win_percentage: float
    goals: int
    assists: int
    last_5_games_goals: int
    last_5_games_assists: int

    class Config:
        orm_mode = True