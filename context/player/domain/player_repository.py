from abc import ABC, abstractmethod
from typing import Optional, List
from .player import Player
from shared.domain.value_objects.player_id import PlayerId


class PlayerRepository(ABC):
    @abstractmethod
    async def find_by_id(self, player_id: PlayerId) -> Optional[Player]:
        pass

    @abstractmethod
    async def save(self, player: Player) -> None:
        pass

    @abstractmethod
    async def find_all(self) -> List[Player]:
        pass

    @abstractmethod
    async def delete(self, player_id: PlayerId) -> bool:
        pass

    @abstractmethod
    async def exists(self, player_id: PlayerId) -> bool:
        pass