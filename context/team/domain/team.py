from typing import List
from backend.shared.domain.aggregate_root import AggregateRoot
from .value_objects.team_id import TeamId

class Team(AggregateRoot):
    def __init__(self, id: TeamId, name: str, players: List[str]):
        self.id = id
        self.name = name
        self.players = players

    @classmethod
    def create(cls, id: TeamId, name: str, players: List[str]) -> 'Team':
        return cls(id, name, players)

    def to_primitives(self) -> dict:
        return {
            "id": self.id.value,
            "name": self.name,
            "players": self.players
        }

    @classmethod
    def from_primitives(cls, plain_data: dict) -> 'Team':
        return cls(
            id=TeamId(plain_data["id"]),
            name=plain_data["name"],
            players=plain_data["players"]
        )