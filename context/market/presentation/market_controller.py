from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from context.market.schemas.market_response import MarketResponse
from context.market.schemas.market_create import MarketCreate


class MarketController:
    # def __init__(self, market_service: market_service):
    def __init__(self,):
        # self.market_service = market_service
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self):
        self.router.post("/", response_model=MarketResponse)(self.create_market)
        self.router.get("/{market_id}", response_model=MarketResponse)(self.get_market)
        self.router.get("/", response_model=list[MarketResponse])(self.get_all_markets)
        self.router.delete("/{market_id}")(self.delete_market)

    async def create_market(self, market: MarketCreate):
        try:
            created_market = await self.market_service.create_market(market)
            if not created_market:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Market could not be created")
            return created_market
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def get_market(self, market_id: str):
        try:
            market = await self.market_service.get_market(market_id)
            if not market:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Market not found")
            return market
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def get_all_markets(self):
        try:
            markets = await self.market_service.get_all_markets()
            return markets
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def delete_market(self, market_id: str):
        try:
            success = await self.market_service.delete_market(market_id)
            if not success:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Market not found")
        except HTTPException as e:
            raise e