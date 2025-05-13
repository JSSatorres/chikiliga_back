from typing import Any
from shared.domain.aggregate_root import AggregateRoot
from .value_objects.player_id import PlayerId

class Player(AggregateRoot):
    def __init__(self, id: PlayerId, name: str, position: str, team: str, point: int = 0):
        self.id = id
        self.name = name
        self.position = position
        self.team = team
        self.point = point

    @classmethod
    def create(cls, id: PlayerId, name: str, position: str, team: str) -> 'Player':
        return cls(id, name, position, team)

    def to_primitives(self) -> dict[str, Any]:
        return {
            "id": self.id.value,
            "name": self.name,
            "position": self.position,
            "team": self.team
        }

    @classmethod
    def from_primitives(cls, plain_data: dict[str, Any]) -> 'Player':
        return cls(
            id=PlayerId(plain_data["id"]),
            name=plain_data["name"],
            position=plain_data["position"],
            team=plain_data["team"]
        )