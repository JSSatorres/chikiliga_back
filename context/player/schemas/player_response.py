from pydantic import BaseModel
from typing import List

class PlayerResponse(BaseModel):
    id: str
    name: str
    position: str
    team: str
    market_value: float

    class Config:
        orm_mode = True

class PlayerListResponse(BaseModel):
    players: List[PlayerResponse]