from backend.context.player.domain.player_repository import PlayerRepository
from backend.context.player.domain.player import Player

class PlayerService:
    def __init__(self, player_repository: PlayerRepository):
        self.player_repository = player_repository

    def create_player(self, player_data):
        player = Player(**player_data)
        return self.player_repository.save(player)

    def get_player(self, player_id):
        return self.player_repository.find(player_id)

    def get_all_players(self):
        return self.player_repository.find_all()

    def update_player(self, player_id, player_data):
        player = Player(**player_data)
        player.id = player_id
        return self.player_repository.save(player)

    def delete_player(self, player_id):
        self.player_repository.delete(player_id)