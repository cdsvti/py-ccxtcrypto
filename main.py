import argparse
import sys
from data.data import fetch_ohlcv_data
from utils.ema import ema
from plot.plotting import plot_ema_and_prices

def main():
    try:
        parser = argparse.ArgumentParser(description='Plot EMAs and actual price for a given symbol.')
        parser.add_argument('symbol', type=str, help='The symbol (e.g., BTCUSDT, ETHUSDT, MATICUSDT)')
        parser.add_argument('--ema-lengths', nargs='+', type=int, default=[8, 21, 56, 80, 100, 200],
                            help='Custom EMA lengths for plotting.')
        parser.add_argument('--limit', type=int, default=300, choices=range(1, 1001),
                            help='Limit the number of data points (1 to 1000). Default is 300.')
        parser.add_argument('--save-png', action='store_true', help='Save the plot as a PNG file.')
        parser.add_argument('--show-price', action='store_true', help='Show the price when hovering over the graph.')

        args = parser.parse_args()

        symbol = args.symbol
        limit = args.limit
        ema_lengths = args.ema_lengths

        # Check if the provided limit is within the range 1 to 1000
        limit = max(1, min(limit, 1000))

        # Fetch historical OHLCV data for the given symbol with the specified limit
        data = fetch_ohlcv_data(symbol, limit=limit)

        # Calculate EMAs
        for length in ema_lengths:
            data[f'EMA_{length}'] = ema(data, length)

        plot_ema_and_prices(data, ema_lengths, symbol, args.save_png, args.show_price)

    except Exception as e:
        print(f"An error occurred: {e}")
        
if __name__ == "__main__":
    main()
