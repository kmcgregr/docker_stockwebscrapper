# Minimal README for the new structure

# Docker Stock Web Scraper

This repository scrapes current stock prices from Google Finance and stores the results in an Excel file and a Markdown table. The scraper is fully configurable via **`config.yaml`** and can run either a one‑off fetch or a continuous scheduler.

## Project layout

```
docker_stockwebscrapper/
├─ README.md
├─ requirements.txt
├─ config.yaml
├─ Dockerfile
├─ docker-compose.yml
├─ src/
│   ├─ __init__.py
│   ├─ config.py
│   ├─ data_loader.py
│   ├─ scraper.py
│   ├─ persistence.py
│   ├─ scheduler.py
│   └─ main.py
├─ tests/
└─ stockwebscrapper/
    ├─ my_stocks.csv
    └─ etf_and_stock_market_data.md
```

## Running locally

```bash
# Install deps
pip install -r requirements.txt
# One‑off scrape
python -m src.main run
# Scheduled scraping (default 10 min + 17:00 daily + Monday weekly)
python -m src.main schedule
```

## Docker / Docker‑Compose

### Build and run

```bash
docker compose up --build
```

The container mounts the `stockwebscrapper` directory, so both the input CSV and the generated output files (`stock_prices.xlsx` and `Stock_prices.md`) persist on the host.

## Configuration

Edit `config.yaml` to change URLs, selectors, header values, schedule timing, or output file names. The default settings already match what the original script used.

## Data format

The Markdown table is written to **`Stock_prices.md`** in the same directory as the Excel file. It looks like:

```
| Stock | Price |
|------|-------|
| AAPL:NASDAQ | 175.32 |
```

## License

MIT
