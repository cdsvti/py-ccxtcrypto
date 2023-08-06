import ccxt
import pandas as pd

def fetch_ohlcv_data(symbol, timeframe='1d', limit=300):
    # Initialize the Binance exchange API
    binance = ccxt.binance()

    # Fetch historical OHLCV data for the given symbol with the specified limit
    ohlcvs = binance.fetch_ohlcv(symbol, timeframe, limit=limit)

    # Convert the data to a DataFrame
    data = pd.DataFrame(ohlcvs, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
    data.set_index('timestamp', inplace=True)

    return data
