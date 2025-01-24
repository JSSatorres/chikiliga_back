from pydantic import BaseModel
from typing import List, Optional

class Player(BaseModel):
    id: Optional[str]  # MongoDB ObjectId
    name: str
    position: str
    market_value: float
    points: List[int]  # Points for each jornada
    goals: List[int]    # Goals for each jornada
    fouls: List[int]    # Fouls for each jornada

    class Config:
        orm_mode = True