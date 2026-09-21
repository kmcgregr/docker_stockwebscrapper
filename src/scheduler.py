import schedule
import time
import datetime
import logging

from .config import load_config
from .data_loader import load_tickers
from .scraper import TickerScraper
from .persistence import save_to_excel, save_to_markdown

logger = logging.getLogger(__name__)

def job() -> None:
    # Only run during weekday business hours
    now = datetime.datetime.now()
    if now.weekday() >= 5:  # Saturday or Sunday
        return
    if not (datetime.time(9, 45) <= now.time() <= datetime.time(17, 0)):
        return
    cfg = load_config()
    tickers = load_tickers('stockwebscrapper/my_stocks.csv')
    scraper = TickerScraper()

    results = []
    for ticker in tickers:
        price = scraper.fetch_price(ticker)
        if price:
            results.append((ticker, price))
        # Polite rate limiting
        time.sleep(5)
    if not results:
        logger.warning("No prices retrieved in this run.")
        return

    excel_path = cfg['persistence']['excel']
    markdown_path = cfg['persistence']['markdown']
    try:
        save_to_excel(results, excel_path)
        save_to_markdown(results, markdown_path)
        logger.info("Saved %s records to %s and %s", len(results), excel_path, markdown_path)
    except Exception as exc:
        logger.error("Failed to persist results: %s", exc)


def schedule_jobs() -> None:
    # Run every 10 minutes during weekday business hours
    schedule.every(10).minutes.do(job)


# expose for main
__all__ = ['schedule_jobs', 'job']
