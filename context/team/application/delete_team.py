from fastapi import HTTPException, status
from context.team.domain.team_repository import TeamRepository
from context.team.domain.value_objects.team_id import TeamId

async def delete_team(team_id: str, team_repository: TeamRepository):
    team_id_value = TeamId(team_id)
    success = await team_repository.delete(team_id_value)
    
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Team not found")