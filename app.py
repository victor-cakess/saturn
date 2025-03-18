import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch Apple stock data
ticker = yf.Ticker("AAPL")
data = ticker.history(period="1y")

# Compute a 50-day moving average
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['Close'], label='Close price')
plt.plot(data.index, data['SMA_50'], label='50-day SMA')
plt.title("AAPL stock price & 50-day moving average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.savefig("chart.png")  # Save plot as an image
print("Chart saved as chart.png")
