import matplotlib.pyplot as plt
import mplcursors
from datetime import datetime

def plot_ema_and_prices(data, ema_lengths, symbol, save_png=False, show_price=False):
    # Plot EMAs and actual price
    plt.figure(figsize=(14, 6))

    for length in ema_lengths:
        if length == 200:
            plt.plot(data.index, data[f'EMA_{length}'], label=f'EMA {length}', color='yellow', linewidth=3)
        else:
            plt.plot(data.index, data[f'EMA_{length}'], label=f'EMA {length}', alpha=0.7)

    plt.plot(data.index, data['close'], label='Actual Price', color='white', linewidth=2)

    last_price = data['close'][-1]
    max_price = data['high'].max()
    min_price = data['low'].min()

    plt.scatter(data.index[-1], last_price, color='white', marker='o', s=30, label=f'Last Price: {last_price:.2f}')
    plt.text(data.index[-1], last_price, f'{last_price:.2f}', color='white', ha='left', va='bottom', fontsize=8, weight='bold')

    plt.scatter(data['high'].idxmax(), max_price, color='red', marker='v', s=50, label=f'Max Price: {max_price:.2f}')
    plt.scatter(data['low'].idxmin(), min_price, color='blue', marker='^', s=50, label=f'Min Price: {min_price:.2f}')

    plt.legend(facecolor='white', edgecolor='white', fontsize=8)
    plt.xlabel('Date', color='white')
    plt.ylabel('Price / EMA Values', color='white')
    plt.title(f'Exponential Moving Averages (EMAs) for {symbol}', color='white')
    plt.grid(color='white', linewidth=0.3, alpha=0.9)

    plt.gca().set_facecolor('#202020')
    plt.gca().set_alpha(0.9)

    plt.tick_params(axis='x', colors='black')
    plt.tick_params(axis='y', colors='black')

    if show_price:
        mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f"Price: {sel.target[1]:.2f}"))

    if save_png:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        plt.savefig(f'{symbol}_ema_plot_{timestamp}.png', bbox_inches='tight', pad_inches=0.0, facecolor=plt.gca().get_facecolor())
        plt.close()
    else:
        plt.show()
