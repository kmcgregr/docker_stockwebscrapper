import argparse
import schedule
import logging


from .scheduler import schedule_jobs, job

# Configure root logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


def main() -> None:
    parser = argparse.ArgumentParser(description='Stock Web Scraper CLI')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('run', help='Run a single scrape and persist results')
    sub.add_parser('schedule', help='Start continuous scheduled scraping')

    args = parser.parse_args()
    if args.command == 'run':
        logging.info('Running one‑off scraping job')
        job()
    else:
        logging.info('Starting scheduled scraper')
        schedule_jobs()
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == '__main__':
    main()
