# py-ccxtcrypto

## Description:
The provided code is a Python function that fetches historical OHLCV (Open, High, Low, Close, Volume) data for a given trading symbol from the Binance exchange using the ccxt library. 

## Import Libraries:
The code imports libraries:
- ccxt: A cryptocurrency trading library that provides an interface to interact with various cryptocurrency exchanges, including Binance.
- pandas: A powerful library for data manipulation and analysis.
- matplotlib.pyplot (as plt): A popular library for creating static, interactive, and animated plots.
- mplcursors: A library that adds data cursor support to Matplotlib plots.
- datetime: A library to work with dates and times.


## Function Definition:
The code defines a function named fetch_ohlcv_data that takes three parameters:
- symbol (str): The trading symbol for which historical data will be fetched (e.g., BTC/USDT, ETH/BTC).
- timeframe (str, optional): The timeframe for the historical data (default is '1d' - daily data). Possible values include '1m', '5m', '15m', '30m', '1h', '1d', '1w', '1M' for minutes, hours, days, weeks, and months, respectively.
- limit (int, optional): The number of data points to fetch (default is 300).
- ema_lengths (list): A list of custom EMA lengths for plotting.
- save_png (bool, optional): A boolean flag indicating whether to save the plot as a PNG file (default is False).
- show_price (bool, optional): A boolean flag indicating whether to show the price when hovering over the graph (default is False).


## Initializing Binance API:

The code initializes the Binance exchange API using the ccxt.binance() function. This creates an instance of the Binance API to interact with the exchange.

Fetching Historical Data:

The fetch_ohlcv method of the Binance API is used to fetch historical OHLCV data for the specified symbol, timeframe, and limit. The data is retrieved as a list of lists, where each inner list represents a single data point with timestamp, open price, high price, low price, close price, and volume.

## Data Conversion to DataFrame:

The fetched data is converted to a Pandas DataFrame using pd.DataFrame. The columns of the DataFrame are labeled as 'timestamp', 'open', 'high', 'low', 'close', and 'volume'.
The 'timestamp' column is converted to Pandas datetime format using pd.to_datetime with the unit 'ms' (milliseconds) since the Binance API provides timestamps in milliseconds.
The 'timestamp' column is set as the DataFrame's index using set_index to facilitate time-based data analysis.

## Data Return:

The function returns the historical OHLCV data as a Pandas DataFrame.
Note: The code assumes that you have already installed the ccxt and pandas libraries in your Python environment for successful execution. You can install them using pip install ccxt pandas. Additionally, you need to have an active internet connection to access data from the Binance exchange through the ccxt library.

The provided code is a Python function that plots Exponential Moving Averages (EMAs) and actual prices using Matplotlib. The function allows you to save the plot as a PNG file or display it interactively, depending on the specified arguments.


## Saving the Plot as PNG (Optional):

If save_png is set to True, the code will save the plot as a PNG file using the current timestamp in the filename.
The datetime.now().strftime("%Y%m%d_%H%M%S") generates a string with the current date and time in the format 'YYYYMMDD_HHMMSS'.
The plot is saved using plt.savefig with additional arguments to adjust the plot's appearance.
The plt.close() is called to close the plot after saving to avoid displaying it interactively.

## Displaying the Plot Interactively:

The plot includes EMAs and actual prices for the specified symbol and EMA lengths.
If show_price is set to True, mplcursors is used to display the price when hovering over the graph.
Note: The code assumes that you have already installed the required libraries, including matplotlib, mplcursors, and datetime. You can install them using pip install matplotlib mplcursors. Additionally, ensure that you have fetched the historical OHLCV data with EMAs using the fetch_ohlcv_data function before calling the plot_ema_and_prices function to plot the data.

## Usage

Here are 5 examples of how to use the Python script main.py with various command-line arguments:

Fetch historical data for BTCUSDT with custom EMA lengths (8, 14, 100, 200), a limit of 200 data points, and save the plot as a PNG file:
```
python3 main.py BTCUSDT --ema-lengths 8 14 100 200 --limit 200 --save-png
```

Fetch historical data for BTCUSDT with custom EMA lengths (8, 14, 100, 200) and a limit of 200 data points. Display the plot interactively without saving as a PNG file:
```
python3 main.py BTCUSDT --ema-lengths 8 14 100 200 --limit 200
```

Fetch historical data for BTCUSDT with custom EMA lengths (8, 14, 100, 200), a limit of 200 data points, and show the price when hovering over the graph:
```
python3 main.py BTCUSDT --ema-lengths 8 14 100 200 --limit 200 --show-price
```

Fetch historical data for ETHUSDT with default EMA lengths (8, 21, 56, 80, 100, 200), a limit of 300 data points, and save the plot as a PNG file:
```
python3 main.py ETHUSDT --limit 300 --save-png
```

Fetch historical data for MATICUSDT with default EMA lengths (8, 21, 56, 80, 100, 200), a limit of 500 data points, and display the plot interactively without saving as a PNG file:

```
python3 main.py MATICUSDT --limit 500
```

Note: Make sure to replace main.py with the actual name of your Python script. The examples demonstrate different combinations of parameters such as the symbol, EMA lengths, limit, saving as PNG, and showing the price. You can customize these arguments based on your specific requirements.

## Disclaimer

The provided Python code is for educational and informational purposes only. It demonstrates how to fetch historical OHLCV data from the Binance exchange using the ccxt library and convert it to a Pandas DataFrame. This code does not constitute financial or investment advice, and it is not intended for actual trading purposes. Use the code at your own risk and discretion. Additionally, please be aware that trading cryptocurrency and financial instruments involves risks, including the potential loss of capital. Always conduct thorough research and consult with a qualified financial advisor before making any investment decisions.