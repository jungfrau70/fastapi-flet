import pandas as pd

def calculate_ema(data: pd.DataFrame, period: int):
    return data['close'].ewm(span=period, adjust=False).mean()
