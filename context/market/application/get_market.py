from typing import Any
from fastapi import HTTPException, status
from context.market.domain.market_repository import MarketRepository
from context.market.domain.market import Market
from context.market.schemas.market_response import MarketResponse

class GetMarket:
    def __init__(self, market_repository: MarketRepository):
        self.market_repository = market_repository

    async def execute(self, market_id: str) -> MarketResponse:
        market = await self.market_repository.get_by_id(market_id)
        if not market:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Market not found")
        return MarketResponse.from_orm(market)