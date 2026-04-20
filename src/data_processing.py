def merge_data(stock_df, news_df):
    merged = stock_df.merge(news_df, on="Date", how="left")
    return merged