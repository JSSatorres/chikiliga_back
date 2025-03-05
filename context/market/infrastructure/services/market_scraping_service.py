from typing import List
import requests
from bs4 import BeautifulSoup
from context.market.domain.market import Market
from context.market.domain.market_repository import MarketRepository

class MarketScrapingService:
    def __init__(self, market_repository: MarketRepository):
        self.market_repository = market_repository

    def scrape_market_data(self, url: str) -> List[Market]:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception("Failed to fetch data from the market URL")

        soup = BeautifulSoup(response.content, 'html.parser')
        market_data = self._parse_market_data(soup)
        return market_data

    def _parse_market_data(self, soup: BeautifulSoup) -> List[Market]:
        markets = []
        # Example parsing logic (this should be adapted to the actual HTML structure)
        for market_item in soup.find_all('div', class_='market-item'):
            market_id = market_item['data-id']
            market_name = market_item.find('h2').text
            market_value = market_item.find('span', class_='value').text

            market = Market(id=market_id, name=market_name, value=market_value)
            markets.append(market)

        return markets

    def save_markets(self, markets: List[Market]):
        for market in markets:
            self.market_repository.save(market)