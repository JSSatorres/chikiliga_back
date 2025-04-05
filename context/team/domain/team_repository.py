from typing import Optional
from abc import ABC, abstractmethod
from context.team.domain.team import Team

class TeamRepository(ABC):
    @abstractmethod
    def get_by_id(self, team_id: str) -> Optional[Team]:
        pass

    @abstractmethod
    def save(self, team: Team) -> Team:
        pass

    @abstractmethod
    def get_all(self) -> list[Team]:
        pass