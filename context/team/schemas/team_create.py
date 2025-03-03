from pydantic import BaseModel
from typing import List

class TeamCreate(BaseModel):
    name: str
    players: List[str]  # List of player IDs that belong to the team

    class Config:
        orm_mode = True