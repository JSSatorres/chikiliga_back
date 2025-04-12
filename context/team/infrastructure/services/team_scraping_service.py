from typing import List
import requests
from bs4 import BeautifulSoup
from context.team.domain.team import Team
from context.team.domain.team_repository import TeamRepository

class TeamScrapingService:
    def __init__(self, team_repository: TeamRepository):
        self.team_repository = team_repository

    def scrape_teams(self) -> List[Team]:
        url = "https://example.com/teams"  # Replace with the actual URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        teams = []
        for team_element in soup.select('.team'):  # Adjust the selector based on the actual HTML structure
            team_name = team_element.select_one('.team-name').text.strip()
            team_id = team_element['data-id']  # Assuming the team ID is stored in a data attribute

            team = Team.create(team_id=team_id, name=team_name)
            teams.append(team)

        return teams

    async def save_scraped_teams(self):
        teams = self.scrape_teams()
        for team in teams:
            await self.team_repository.save(team)