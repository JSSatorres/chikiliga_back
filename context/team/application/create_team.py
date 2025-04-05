from typing import Any
from fastapi import HTTPException, status
from context.team.domain.team_repository import TeamRepository
from context.team.schemas.team_create import TeamCreate
from context.team.domain.team import Team

class CreateTeam:
    def __init__(self, team_repository: TeamRepository):
        self.team_repository = team_repository

    async def execute(self, team_create: TeamCreate) -> Team:
        try:
            team = Team.create(**team_create.dict())
            return await self.team_repository.save(team)
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))