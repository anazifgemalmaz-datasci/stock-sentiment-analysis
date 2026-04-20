import yfinance as yf

def get_stock_data(ticker="AAPL"):
    df = yf.download(ticker,start="2020-01-01",end="2024-01-01")
    return df
 
