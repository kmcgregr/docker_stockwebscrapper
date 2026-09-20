import os
import sys
import requests
import csv
import pandas as pd
import schedule
import time

from bs4 import BeautifulSoup

def read_stock_file():
    with open('my_stocks.csv', 'r') as stock_data_file:
        return stock_data_file.readlines()

def get_stock_price():
    list_of_stock_tickers = []
    list_of_stock_prices = []
    stock_tickers = read_stock_file()

    for stock in stock_tickers:
        stock = stock.strip()
        if not stock:
            continue
        try:
            print(f"Fetching: {stock}")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/124.0.0.0 Safari/537.36'
            }

            # Updated URL format to match current Google Finance beta structure
            url = f"https://www.google.com/finance/beta/quote/{stock}"
            print(f"URL: {url}")
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')

            # --- Updated selector based on current DOM structure ---
            # Target: div.N6SYTe > span[jsname="Pdsbrc"] > span (inner price span)
            price = None

            container = soup.find('div', class_='N6SYTe')
            if container:
                pdsbrc_span = container.find('span', {'jsname': 'Pdsbrc'})
                if pdsbrc_span:
                    inner_span = pdsbrc_span.find('span')
                    if inner_span:
                        price = inner_span.text.strip()

            # Fallback: try the old selector in case Google reverts
            if not price:
                old_element = soup.find('div', class_='YMlKec fxKbKc')
                if old_element:
                    price = old_element.text.strip()

            # Strip currency symbols
            if price:
                price = price.replace('CA', '').strip()

            if price:
                print(f"Stock: {stock}  |  Price: {price}")
                list_of_stock_tickers.append(stock)
                list_of_stock_prices.append(price)
                time.sleep(5)  # Be polite — avoid rate limiting
            else:
                print(f"WARNING: Price element not found for {stock}. Page structure may have changed again.")

        except Exception as error:
            print(f"ERROR fetching {stock}: {error.args[0]}")
            sys.exit()

    print("\nTickers:", list_of_stock_tickers)
    print("Prices: ", list_of_stock_prices)

    data_t = {'stock': list_of_stock_tickers, 'price': list_of_stock_prices}
    df = pd.DataFrame.from_dict(data_t)

    df.to_excel("stock_prices.xlsx", index=False)
    print("Saved to stock_prices.xlsx")


schedule.every(10).minutes.do(get_stock_price)
schedule.every().day.at("17:00").do(get_stock_price)
schedule.every().monday.do(get_stock_price)

print("Stock scraper scheduled. Running first fetch now...")
get_stock_price()  # Run immediately on startup

while True:
    schedule.run_pending()
    time.sleep(1)