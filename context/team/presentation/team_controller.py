from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from context.team.schemas.team_response import TeamResponse
from context.team.schemas.team_create import TeamCreate
# from context.team.application.team_service import TeamService


class TeamController:
    # def __init__(self, team_service: TeamService):
    def __init__(self):
        # self.team_service = team_service
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self):
        self.router.post("/", response_model=TeamResponse)(self.create_team)
        self.router.get("/{team_id}", response_model=TeamResponse)(self.get_team)
        self.router.get("/", response_model=list[TeamResponse])(self.get_all_teams)
        self.router.delete("/{team_id}")(self.delete_team)

    async def create_team(self, team: TeamCreate):
        try:
            created_team = await self.team_service.create_team(team)
            if not created_team:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Team could not be created")
            return created_team
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def get_team(self, team_id: str):
        try:
            team = await self.team_service.get_team(team_id)
            if not team:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team not found")
            return team
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def get_all_teams(self):
        try:
            teams = await self.team_service.get_all_teams()
            return teams
        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    async def delete_team(self, team_id: str):
        try:
            success = await self.team_service.delete_team(team_id)
            if not success:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team not found")
        except HTTPException as e:
                raise e 