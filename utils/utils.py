from datetime import datetime

import pandas as pd
from pandas import DataFrame


def parse(data) -> DataFrame:
    parsed_data = [{'date': datetime.strptime(item['date'], '%Y-%m-%d'), 'price': item['price']}
                   for item in data]

    df = pd.DataFrame(parsed_data)

    return df


class Utils:
    def __init__(self):
        pass
