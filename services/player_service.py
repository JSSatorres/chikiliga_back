from db.mongo_connection import mongo_connection

class PlayerService:
    def __init__(self):
        self.collection = mongo_connection.get_database()["players"]

    def add_player(self, player_data):
        self.collection.insert_one(player_data)

    def get_all_players(self):
        return list(self.collection.find({}))

    def find_player_by_name(self, name):
        return self.collection.find_one({"name": name})

player_service = PlayerService()