import os
import json
from datetime import *
from DataLoaderModels import *

class InvalidDataException(Exception):
    "Invalid Data"
    pass


class DataTransformer:
    def sort_data(self, date_price_list):
        date_price_list.sort(key=lambda date_price: date_price.get_date())
        for date_price in date_price_list:
            time_price_list = date_price.get_time_price_list()
            time_price_list.sort(key=lambda time_price: time_price.get_time())
            date_price.set_time_price_list(time_price_list)

    def _get_time_price_list(self, data, date):
        date_data = list(filter(lambda x: x[0].date() == date, data))
        return list(map(lambda row: TimePrice(row[0].time(), row[1]), date_data))

    def transform(self, data):
        d1 = list(map(lambda row: [datetime.fromtimestamp(row[0]), row[1]], data))
        all_dates = set(map(lambda row: (row[0]).date(), d1))
        result = []
        for cur_date in all_dates:
            result.append(DatePrice(cur_date, self._get_time_price_list(d1, cur_date)))
        self.sort_data(result)
        return result


class DataFetcher:
    MARKET_CLOSE_TIME = "15:29:00"
    MARKET_OPEN_TIME = "09:15:00"

    def _add_data(self, new_data, all_data, filename):
        timestamp_list = new_data['chart']['result'][0]['timestamp']
        prices_list = new_data['chart']['result'][0]['indicators']['quote'][0]['close']

        assert len(timestamp_list) == len(prices_list), \
            "Size mismatch of timestamp and prices " + str(len(timestamp_list)) + " " + \
            str(len(prices_list)) + " " + filename

        for timestamp, price in zip(timestamp_list, prices_list):
            all_data[timestamp] = price

    def fetch_data(self, directory_path):
        all_data = dict()
        for filename in os.listdir(directory_path):
            with open(os.path.join(directory_path, filename), 'r') as f:
                single_file_data = json.load(f)
                self._add_data(single_file_data, all_data, filename)

        all_data = list(all_data.items())
        return all_data


class DataVerifier:
    MINUTES_DURING_MARKET_OPEN = 375

    def verify_data(self, date_price_list):
        for date_price in date_price_list:
            time_price_list = date_price.get_time_price_list()
            assert len(time_price_list) == self.MINUTES_DURING_MARKET_OPEN, "Full day data not present " + str(
                date_price.get_date()) + "  " + str(len(time_price_list))


class DataLoader:
    def load_data(self, directory_path):
        df = DataFetcher()
        data = df.fetch_data(directory_path)
        transformer = DataTransformer()
        transform_data = transformer.transform(data)
        dv = DataVerifier()
        dv.verify_data(transform_data)
        return transform_data


dl = DataLoader()
data = dl.load_data("../data/icici/")
print(data)
