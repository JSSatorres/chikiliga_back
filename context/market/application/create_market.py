from typing import Any
from fastapi import HTTPException, status
from context.market.domain.market_repository import MarketRepository
from context.market.domain.market import Market
from context.market.schemas.market_create import MarketCreate

class CreateMarket:
    def __init__(self, market_repository: MarketRepository):
        self.market_repository = market_repository

    async def execute(self, market_create: MarketCreate) -> Market:
        try:
            market = Market.create(**market_create.dict())
            return await self.market_repository.save(market)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))