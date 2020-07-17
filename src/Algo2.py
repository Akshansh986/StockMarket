from DataLoader import DataLoader
from Infrastructure import *


class Util(object):
    def flatten(self, date_price_list):
        print("Flattening data")
        result = []
        for date_price in date_price_list:
            for time_price in date_price.get_time_price_list():
                result.append(time_price.get_price())

        filtered_result = [x for x in result if x is not None]
        print("Total data ponits : " + str(len(result)))
        print("Final data points after null filter : " + str(len(filtered_result)))
        return filtered_result




def start_trading(market, account, max_price, min_price):
    while True:
        market_opened = market.tick()
        if not market_opened:
            break

        price = market.get_price()
        if price is None:
            continue






# dl = DataLoader()
# util = Util()
# date_price_list = dl.load_data("../data/icici/")
# account = Account()
#
# account.deposit_amount(50000)
# flattened_prices = util.flatten(date_price_list)
# max_price = max(flattened_prices)
# min_price = min(flattened_prices)
#
# for date_price in date_price_list:
#     market = Market(date_price)
#     start_trading(market, account, max_price, min_price)

    # print("Statement after:", date_price.get_date(), "StartTime:", start_time)
    # account.print_statement()