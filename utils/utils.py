from datetime import datetime

import pandas as pd


def parse(data):
    parsed_data = [{'date': datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S').date(), 'price': item['price']}
                   for item in data]

    df = pd.DataFrame(parsed_data)

    return df


class Utils:
    def __init__(self):
        pass

