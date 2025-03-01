from shared.domain.value_objects import PlayerId, PlayerName, PlayerEmail, PlayerPosition

class Player:
    def __init__(self, player_id: PlayerId, name: PlayerName, email: PlayerEmail, team: str, position: PlayerPosition, points: int = 0):
        self.id = player_id
        self.name = name
        self.email = email
        self.team = team
        self.position = position
        self.points = points

    @classmethod
    def create(cls, player_id: str, name: str, email: str, team: str, position: str):
        return cls(PlayerId(player_id), PlayerName(name), PlayerEmail(email), team, PlayerPosition(position))

    def update_email(self, new_email: str):
        self.email = PlayerEmail(new_email)

    def to_dict(self):
        return {
            "id": self.id.value,
            "name": self.name.value,
            "email": self.email.value,
            "team": self.team,
            "position": self.position.value,
            "points": self.points
        }
