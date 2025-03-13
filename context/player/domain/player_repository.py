from abc import ABC, abstractmethod
from typing import Optional, List
from .player import Player

class PlayerRepository(ABC):
    @abstractmethod
    def get_by_id(self, player_id: str) -> Optional[Player]:
        pass

    @abstractmethod
    def save(self, player: Player) -> Player:
        pass

    @abstractmethod
    def get_all(self) -> List[Player]:
        pass