import time
import requests
from bs4 import BeautifulSoup
import logging

from .config import load_config

logger = logging.getLogger(__name__)

class TickerScraper:
    def __init__(self):
        cfg = load_config()
        self.url_template = cfg['scraper']['url_template']
        self.selectors = cfg['scraper']['selectors']
        self.headers = cfg['scraper']['headers']
        self.currency_strip = cfg['scraper'].get('currency_strip', [])

    def fetch_price(self, ticker: str) -> str | None:
        """Return the current price string for the ticker.
        Returns None if price element not found.
        """
        url = self.url_template.format(ticker=ticker)
        try:
            resp = requests.get(url, headers=self.headers, timeout=10)
            resp.raise_for_status()
        except Exception as exc:
            logger.error("Network error for %s: %s", ticker, exc)
            return None

        soup = BeautifulSoup(resp.content, 'html.parser')
        price = None
        for sel in self.selectors:
            elem = soup.select_one(sel)
            if elem:
                price = elem.get_text(strip=True)
                break
        if not price:
            logger.warning("Price not found for %s", ticker)
            return None
        # Strip unwanted currency prefixes/suffixes
        for prefix in self.currency_strip:
            price = price.replace(prefix, '').strip()
        return price

# Example: scraper = TickerScraper(); price = scraper.fetch_price('AAPL:NASDAQ')
