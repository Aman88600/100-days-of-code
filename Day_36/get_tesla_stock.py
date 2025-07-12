import yfinance as yf

# Tesla's ticker symbol
tesla = yf.Ticker("TSLA")

def get_stock():
    # Get the current market price
    price_1 = tesla.history(period="2d")["Close"].iloc[0]
    price_2 = tesla.history(period="1d")["Close"].iloc[0]

    price_change = price_2 - price_1

    # calaculating the percentage
    change_percentage = (abs(price_change) * 100)/price_1

    if price_change > 0:
        return f"Stock has gone up by {change_percentage:.2f} %"
    elif price_change < 0:
        return "Stock has gone down by {change_percentage:.2f} %"
    else:
        return "No change in stock"