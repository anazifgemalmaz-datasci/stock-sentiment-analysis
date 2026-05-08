import yfinance as yf
import pandas as pd

def get_stock_data(ticker="AAPL"):
    df = yf.download(ticker,start="2020-01-01",end="2024-01-01")
    
    df = df[["Open","Close","Volume"]]
    df.reset_index(inplace=True) #date'i index'ten sütuna çevir
    df.columns= ["Date","Open","Close","Volume"]
    df["Date"]=pd.to_datetime(df["Date"]).dt.date
    
    return df
    


def get_news_data():
    print("Haber verisi hazırlanıyor")
    #Burası sahte veri üretecek. Sonrasında NewsAPI ve scraping kodumuz yerine gelecek.
    mock_data= {
        'Data': pd.to_datetime(["2023-12-28","2023-12-29","2024-01-01"]).date,
        'Headline' : [
            "Apple sees record breaking sales in holiday season",
            "Supply chain issues might hit tech giants",
            "New iPhone production delayed"
        ]
    }
    return pd.DataFrame(mock_data)