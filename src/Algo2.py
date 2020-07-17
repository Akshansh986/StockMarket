from DataLoader import DataLoader
from Infrastructure import *
from Util import *


def start_trading(market, account, buy_price, sell_price):
    while True:
        market_opened = market.tick()
        if not market_opened:
            break

        price = market.get_price()
        if price is None:
            continue

        if market.get_price() <= buy_price and account.get_balance() > 0:
            # print ("Buying at :", market.get_price())
            account.buy_stock(market.get_price())
            # account.print_statement()

        if market.get_price() >= sell_price and account.get_stock() > 0:
            # print("Selling at : ", market.get_price())
            account.sell_stock(market.get_price())
            # account.print_statement()

    account.sell_stock(account.get_last_purchase_price())


dl = DataLoader()
util = Util()
date_price_list = dl.load_data("../data/icici/")
flattened_prices = util.flatten(date_price_list)
max_price = int(max(flattened_prices))
min_price = int(min(flattened_prices))
print( "Min Price", min_price, "Max Price", max_price)


# start_trading(market, account, 345, 360)
# account.print_statement()

optimal_buy = 0
optimal_sell = 0
optimal_num_trades = 0
max_profit = 0
for buy_price in range(min_price, max_price):
    for sell_price in range(min_price, max_price):
        account = Account()
        account.deposit_amount(100000)
        market = Market(flattened_prices)

        start_trading(market, account, buy_price, sell_price)
        if account.get_balance() > max_profit:
            optimal_buy = buy_price
            optimal_sell = sell_price
            max_profit = account.get_balance()
            optimal_num_trades = account.get_num_trades()

print("Max Profit : ", max_profit, ", Buy at : ", optimal_buy, ", Sell at : ", optimal_sell, ", Num trades : ", optimal_num_trades)
