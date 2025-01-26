from pydantic import BaseModel
from typing import List, Optional

class PlayerBase(BaseModel):
    name: str
    market_value: float
    minimum_offer: float

class PlayerCreate(PlayerBase):
    pass

class PlayerUpdate(PlayerBase):
    market_value: Optional[float] = None
    minimum_offer: Optional[float] = None

class Player(PlayerBase):
    id: str

    class Config:
        orm_mode = True

class PlayerList(BaseModel):
    players: List[Player]