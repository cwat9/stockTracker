from yahoo_fin.stock_info import *

dow = tickers_dow()
nasdaq = tickers_nasdaq()
sp500 = tickers_sp500()
other = tickers_other()

list = ["dow", "nasdaq", "sp500", "other"]

def switch(argument):
    if argument == 'dow':
        return dow
    elif argument == 'nasdaq':
        return nasdaq
    elif argument == 'sp500':
        return sp500
    elif argument == "other":
        return other

def generate_stocks():
    for i in list:
        with open("stocks/"+i+".txt", "w") as f:
            f.write(str(switch(i)))