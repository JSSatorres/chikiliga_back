from pydantic import BaseModel, Field

class PlayerCreate(BaseModel):
    name: str = Field(..., description="The name of the player")
    age: int = Field(..., ge=0, description="The age of the player")
    position: str = Field(..., description="The position of the player")
    team_id: str = Field(..., description="The ID of the team the player belongs to")