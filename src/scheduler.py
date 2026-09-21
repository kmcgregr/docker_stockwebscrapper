import schedule
import time
import logging

from .config import load_config
from .data_loader import load_tickers
from .scraper import TickerScraper
from .persistence import save_to_excel, save_to_markdown

logger = logging.getLogger(__name__)

def job() -> None:
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
    cfg = load_config()
    minutes = cfg['schedule'].get('minutes', 10)
    daily_at = cfg['schedule'].get('daily_at')
    weekly_day = cfg['schedule'].get('weekly_day')

    schedule.every(minutes).minutes.do(job)
    if daily_at:
        schedule.every().day.at(daily_at).do(job)
    if weekly_day:
        schedule.every(weekly_day).do(job)


# expose for main
__all__ = ['schedule_jobs', 'job']
