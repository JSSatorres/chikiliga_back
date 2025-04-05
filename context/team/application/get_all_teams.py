from typing import List
from context.team.domain.team_repository import TeamRepository
from context.team.domain.team import Team

class GetAllTeams:
    def __init__(self, team_repository: TeamRepository):
        self.team_repository = team_repository

    async def execute(self) -> List[Team]:
        return await self.team_repository.get_all()