import os
import sys
import requests
import csv
import pandas as pd
import datetime
import schedule
import time

from bs4 import BeautifulSoup

def read_stock_file():
 stock_data_file = open('my_stocks.csv','r')
 return stock_data_file.readlines()
 
def get_stock_price():
    list_of_stock_stickers =[]
    list_of_stock_prices = []
    stock_tickers = read_stock_file()
    for stock in stock_tickers:
        try:
            print("Stock",stock)
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
            
            url= "https://www.google.com/finance/quote/%s"%(stock)
            print (url)
            page = requests.get(url,headers=headers)
            
            soup = BeautifulSoup(page.content, 'html.parser')
            
            
            stock_price = soup.find('div', class_='YMlKec fxKbKc')
            price = stock_price.text
            print("Stock :",stock," stock price: ", price)
            list_of_stock_stickers.append(stock.strip())
            list_of_stock_prices.append(price)
            time.sleep(5)
        except Exception as error:
            print("An error occured",error.args[0])
            sys.exit()
    print(list_of_stock_stickers)
    data_t = {'stock': list_of_stock_stickers,'price': list_of_stock_prices}
    df = pd.DataFrame.from_dict(data_t)
    df.to_excel("stock_prices.xlsx")

get_stock_price()
#schedule.every(10).minutes.do(get_stock_price)
#schedule.every().day.at("17:00").do(get_stock_price)
#schedule.every().monday.do(get_stock_price)
#print("I am scheduling the web scrapper")
#while True:
#  schedule.run_pending()
#  time.sleep(1)


 

