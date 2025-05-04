from pydantic import BaseModel, Field
from typing import List

class MarketCreate(BaseModel):
    name: str = Field(..., description="The name of the market")
    players: List[str] = Field(..., description="List of player IDs in the market")
    status: str = Field(..., description="The status of the market (e.g., active, inactive)")   
    created_at: str = Field(..., description="The creation timestamp of the market")