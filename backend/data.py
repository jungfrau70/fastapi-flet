import pandas as pd
from datetime import datetime, timedelta
import random

def generate_ohlc_data(days: int = 100):
    base = datetime.today()
    date_list = [base - timedelta(days=x) for x in range(days)]
    data = {
        'timestamp': [date.strftime('%Y-%m-%dT%H:%M:%S.%fZ') for date in date_list],
        'open': [random.uniform(100, 200) for _ in range(days)],
        'high': [random.uniform(200, 300) for _ in range(days)],
        'low': [random.uniform(50, 100) for _ in range(days)],
        'close': [random.uniform(100, 200) for _ in range(days)]
    }

    # print(data)
    # print(type(data))
    return pd.DataFrame(data)
