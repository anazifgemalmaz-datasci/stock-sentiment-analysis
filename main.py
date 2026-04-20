from src.data_collection import get_stock_data

def main():
    df = get_stock_data()
    print(df.head())

if __name__ == "__main__":
    main()