from pymongo import MongoClient
from bson import ObjectId
from context.market.domain.market_repository import MarketRepository
from context.market.domain.market import Market

class MongoMarketRepository(MarketRepository):
    def __init__(self, db_url: str, db_name: str):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db['markets']

    def get_by_id(self, market_id: str) -> Market:
        data = self.collection.find_one({"_id": ObjectId(market_id)})
        return Market(**data) if data else None

    def save(self, market: Market) -> Market:
        self.collection.update_one({"_id": market.id}, {"$set": market.to_dict()}, upsert=True)
        return market

    def get_all(self):
        return [Market(**data) for data in self.collection.find()]