from fastapi import HTTPException, status
from context.market.domain.market_repository import MarketRepository
from context.market.domain.value_objects.market_id import MarketId

class DeleteMarket:
    def __init__(self, market_repository: MarketRepository):
        self.market_repository = market_repository

    async def execute(self, market_id: str):
        market_id_value = MarketId(market_id)
        success = await self.market_repository.delete(market_id_value)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Market not found"
            )