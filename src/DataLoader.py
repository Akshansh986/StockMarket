import os
import json
from datetime import *

class InvalidDataException(Exception):
    "Invalid Data"
    pass


class DataView:

    def __init__(self, data):
        self.data = data

    # def get_by_date(self, ):

class DataLoader:

    def _sort_function(self, e):
        return e[0]

    def _verify_data_consistency(self, all_data):


    def _add_data(self, new_data, all_data, filename):
        timestamp_list = new_data['chart']['result'][0]['timestamp']
        prices_list = new_data['chart']['result'][0]['indicators']['quote'][0]['close']

        assert len(timestamp_list) == len(prices_list), \
            "Size mismatch of timestamp and prices " + str(len(timestamp_list)) + " " +\
            str(len(prices_list)) + " " + filename

        for timestamp, price in zip(timestamp_list, prices_list):
            all_data[timestamp] = price

    def get_data(self, directory_path):
        all_data = dict()
        for filename in os.listdir(directory_path):
            with open(os.path.join(directory_path, filename), 'r') as f:
                single_file_data = json.load(f)
                self._add_data(single_file_data, all_data, filename)

        all_data = list(all_data.items())
        all_data.sort(key=self._sort_function)
        self._verify_data_consistency(all_data)
        return all_data
#
# dl = DataLoader()
# data = dl.get_data("../data/icici/")
# print(data)
# print(data[0][0])

dt = datetime.fromtimestamp(1586749500)
print(dt.time())