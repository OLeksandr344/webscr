import yfinance as yf

def get_stock_data(ticker):
    stock_info = yf.Ticker(ticker)
    stock_history = stock_info.history(period="1d") 

    return stock_history
ticker = "BTC-USD" 
stock_data = get_stock_data(ticker)
print(f"\nCurrency data for {ticker}:")
print(stock_data)
