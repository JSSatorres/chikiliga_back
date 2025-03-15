from typing import List
import requests
from bs4 import BeautifulSoup
from context.player.domain.player import Player

class PlayerScrapingService:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def scrape_players(self) -> List[Player]:
        response = requests.get(self.base_url)
        if response.status_code != 200:
            raise Exception("Failed to fetch data from the external source")

        soup = BeautifulSoup(response.content, 'html.parser')
        players = self._parse_players(soup)
        return players

    def _parse_players(self, soup: BeautifulSoup) -> List[Player]:
        player_list = []
        # Assuming players are listed in a table with class 'player-table'
        for row in soup.select('.player-table tr'):
            columns = row.find_all('td')
            if columns:
                player_id = columns[0].text.strip()
                player_name = columns[1].text.strip()
                # Add more fields as necessary
                player = Player(id=player_id, name=player_name)
                player_list.append(player)
        return player_list