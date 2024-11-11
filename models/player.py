from pydantic import BaseModel
from typing import Optional

class Player(BaseModel):
    name: str
    team: Optional[str] = None
    position: Optional[str] = None
    market_value: Optional[float] = None