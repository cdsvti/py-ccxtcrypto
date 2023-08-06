def ema(data, length):
    return data['close'].ewm(span=length, adjust=False).mean()
