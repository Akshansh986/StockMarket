from DataLoader import DataLoader
from Infrastructure import *

def start_trading(market, start_time, account):
    while True:
        market_opened = market.tick()
        if not market_opened:
            break

        price = market.get_price()
        if price is None:
            continue

        if market.get_time() == start_time:
            account.buy_stock(price)
            continue

        if market.get_time() > start_time:
            if account.get_stock() > 0:
                difference = price - account.get_last_purchase_price()
                if difference <= -.1:
                    account.sell_stock(price)
                elif difference >= 4:
                    account.sell_stock(price)
                    break
            else:
                difference = price - account.get_last_purchase_price()
                if difference >= 0:
                    account.buy_stock(price)

    account.sell_stock(market.get_market_close_price())





dl = DataLoader()
date_price_list = dl.load_data("../data/icici/")

account = Account()
account.deposit_amount(50000)
for date_price in date_price_list:
    market = DayMarket(date_price)
    start_time = date_price.get_time_price_list()[10].get_time()

    start_trading(market, start_time, account)

    print("Statement after:", date_price.get_date(), "StartTime:", start_time)
    account.print_statement()