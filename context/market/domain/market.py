from backend.shared.domain.aggregate_root import AggregateRoot
from .value_objects.market_id import MarketId

class Market(AggregateRoot):
    def __init__(self, id: MarketId, name: str, players: list):
        self.id = id
        self.name = name
        self.players = players

    @staticmethod
    def create(id: MarketId, name: str, players: list) -> 'Market':
        return Market(id, name, players)

    def to_primitives(self) -> dict:
        return {
            "id": self.id.value,
            "name": self.name,
            "players": self.players
        }

    @staticmethod
    def from_primitives(data: dict) -> 'Market':
        return Market(
            id=MarketId(data['id']),
            name=data['name'],
            players=data['players']
        )