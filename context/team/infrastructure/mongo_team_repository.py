from pymongo import MongoClient
from bson import ObjectId
from context.team.domain.team_repository import TeamRepository
from context.team.domain.team import Team

class MongoTeamRepository(TeamRepository):
    def __init__(self, db_url: str, db_name: str):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.collection = self.db['teams']

    def get_by_id(self, team_id: str) -> Team:
        data = self.collection.find_one({"_id": ObjectId(team_id)})
        return Team.from_primitives(data) if data else None

    def save(self, team: Team) -> Team:
        self.collection.update_one({"_id": team.id.value}, {"$set": team.to_primitives()}, upsert=True)
        return team

    def get_all(self):
        return [Team.from_primitives(data) for data in self.collection.find()]