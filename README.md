# Docker Stock Web Scraper

This repository contains a simple Python script that scrapes the current price of a list of stock tickers from Google Finance and writes the results to an Excel file. The application runs inside a Docker container and can be scheduled to run at regular intervals.

## Prerequisites
- Docker (≥ 19.03)
- Docker Compose (optional)

## Local development
```bash
python -m pip install -r requirements.txt
python stock_web_scrapper.py
```

## Docker
```bash
docker build -t stockwebscrapper .
docker run --rm -v "$(pwd)/stockwebscrapper:/usr/src/app" stockwebscrapper
```

## Docker Compose
```bash
docker-compose up --build
```

The container mounts the `stockwebscrapper` directory so that `my_stocks.csv` and the generated `stock_prices.xlsx` are persisted on the host.

## Configuration
The script reads the list of tickers from `stockwebscrapper/my_stocks.csv`.  The default schedule is:
- every 10 minutes
- every day at 17:00
- every Monday

Feel free to change the schedule in `stock_web_scrapper.py`.

## Testing
Run tests with pytest:
```bash
pytest
```

## License
MIT
