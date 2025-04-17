from pydantic import BaseModel
from typing import List

class PlayerResponse(BaseModel):
    id: str
    name: str
    position: str
    team: str

class TeamResponse(BaseModel):
    id: str
    name: str
    players: List[PlayerResponse]

    class Config:
        orm_mode = True

    def to_primitives(self):
        return {
            "id": self.id,
            "name": self.name,
            "players": [player.dict() for player in self.players]
        }

    @classmethod
    def from_primitives(cls, data):
        players = [PlayerResponse(**player) for player in data.get("players", [])]
        return cls(id=data["id"], name=data["name"], players=players)