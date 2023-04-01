import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def calculate_moving_average(data, window_size):
    return data['Close'].rolling(window=window_size).mean()

def calculate_daily_returns(data):
    return data['Close'].pct_change().dropna()

def plot_closing_prices(data, ticker):
    plt.plot(data.index, data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.title(f'{ticker} Closing Prices')
    plt.show()

def plot_moving_average(data, window_size):
    plt.plot(data.index, data['Close'], label='Close')
    plt.plot(data.index, data[f'MA{window_size}'], label=f'MA{window_size}')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{window_size}-Day Moving Average')
    plt.legend()
    plt.show()

def main():
    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = datetime.today().strftime('%Y-%m-%d')
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    window_size = 50
    stock_data[f'MA{window_size}'] = calculate_moving_average(stock_data, window_size)

    stock_data['Daily Returns'] = calculate_daily_returns(stock_data)

    plot_closing_prices(stock_data, ticker)

    plot_moving_average(stock_data, window_size)

if __name__ == "__main__":
    main()
