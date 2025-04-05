from typing import Optional
from fastapi import HTTPException, status
from context.team.domain.team_repository import TeamRepository
from context.team.domain.team import Team

class GetTeam:
    def __init__(self, team_repository: TeamRepository):
        self.team_repository = team_repository

    async def execute(self, team_id: str) -> Optional[Team]:
        team = await self.team_repository.get_by_id(team_id)
        if not team:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team not found")
        return team