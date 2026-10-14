import yfinance as yf
import os

# List of your 10 stock tickers
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'JPM', 'V', 'DIS']

# Folder to save CSVs
folder = 'stock_data'
os.makedirs(folder, exist_ok=True)

# Download historical data for each stock
for stock in tickers:
    print(f"Downloading data for {stock}...")
    df = yf.download(stock, start='2013-01-01', end='2023-01-01', progress=False, auto_adjust=True)
    df.to_csv(os.path.join(folder, f'{stock}.csv'))
    print(f"Saved {stock}.csv")

print("All data downloaded and saved in the 'stock_data' folder.")
