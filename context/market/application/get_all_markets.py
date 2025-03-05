from typing import List
from fastapi import HTTPException, status
from context.market.domain.market_repository import MarketRepository
from context.market.schemas.market_response import MarketResponse

class GetAllMarkets:
    def __init__(self, market_repository: MarketRepository):
        self.market_repository = market_repository

    async def execute(self) -> List[MarketResponse]:
        markets = await self.market_repository.get_all()
        if not markets:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No markets found")
        return [MarketResponse.from_orm(market) for market in markets]