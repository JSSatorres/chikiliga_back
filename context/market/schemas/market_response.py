from pydantic import BaseModel
from typing import List

class MarketResponse(BaseModel):
    id: str
    name: str
    players: List[str]  # List of player IDs in the market
    status: str  # e.g., "active", "closed"

    class Config:
        orm_mode = True

    def to_primitives(self):
        return {
            "id": self.id,
            "name": self.name,
            "players": self.players,
            "status": self.status,
        }

    @classmethod
    def from_primitives(cls, data):
        return cls(
            id=data["id"],
            name=data["name"],
            players=data["players"],
            status=data["status"],
        )