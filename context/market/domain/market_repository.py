from typing import Optional, List
from abc import ABC, abstractmethod
from context.market.domain.market import Market

class MarketRepository(ABC):
    @abstractmethod
    def get_by_id(self, market_id: str) -> Optional[Market]:
        pass

    @abstractmethod
    def save(self, market: Market) -> Market:
        pass

    @abstractmethod
    def get_all(self) -> List[Market]:
        pass