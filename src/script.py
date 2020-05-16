from DataLoader import DataLoader


class Market:
    def __init__(self, date_price):
        self.date_price = date_price
        self.time_price_list = date_price.get_time_price_list()
        self.cur_index = -1

    def get_date(self):
        return date_price.get_date()

    def get_time(self):
        return self.time_price_list[self.cur_index].get_time()

    def tick(self):
        self.cur_index = self.cur_index + 1
        return False if self.cur_index >= len(self.time_price_list) else True

    def get_price(self):
        return self.time_price_list[self.cur_index].get_price()

    def get_last_price(self):
        return self.time_price_list[self.cur_index-1].get_price()


class Account:
    def __init__(self):
        self.balance = 0
        self.stock = 0
        self.lastPurchasePrice = -1
        self.lastSoldPrice = -1

    def deposit_amount(self, amount):
        # print("Deposited Amount " + str(amount))
        self.balance = self.balance + amount
        # self.printStatement()

    def withdraw_amount(self, amount):
        if amount > self.balance:
            raise Exception("Sorry, insufficient balance!!!")
            # print("withdrawAmount " + str(amount))
        self.balance = self.balance - amount
        # self.printStatement()

    def buy_stock(self, stockPrice):
        # print("Buy Stock at " + str(stockPrice))
        self.stock = self.stock + (self.balance / stockPrice)
        self.balance = 0
        self.lastPurchasePrice = stockPrice
        # self.printStatement()

    def sell_stock(self, stockPrice):
        # print("Sell Stock at " + str(stockPrice))
        self.balance = self.balance + (stockPrice * self.stock)
        self.stock = 0
        self.lastSoldPrice = stockPrice
        # self.printStatement()

    def print_statement(self):
        print("-------------")
        print("Bank Balance " + str(self.balance))
        print("Stocks " + str(self.stock))
        # print("Last purchase price " + str(self.lastPurchasePrice))
        # print("Last sold price " + str(self.lastSoldPrice))
        print("-------------")
        print("")

    def get_balance(self):
        return self.balance

    def get_stock(self):
        return self.stock

    def get_last_purchase_price(self):
        return self.lastPurchasePrice

    def get_last_sold_price(self):
        return self.lastSoldPrice


def evaluate(market,  start_time):
    account = Account()
    account.deposit_amount(50000)

    while True:
        market_opened = market.tick()
        if not market_opened:
            break

        price = market.get_price()
        if price is None:
            continue
        last_price = market.get_last_price();

        if market.get_time() == start_time:
            # print("Purchasing stock at " + str(price))
            account.buy_stock(price)
            continue

        if market.get_time() > start_time:
            if account.get_stock() > 0:
                difference = price - account.get_last_purchase_price()
                if difference <= -.1:
                    account.sell_stock(price)
                elif difference >= 4:
                    account.sell_stock(price)
                    # print("Purchase done!!!")
                    break
            else:
                difference = price - account.get_last_purchase_price()
                if difference >= 0:
                    account.buy_stock(price)

    print("Evaluation for ", market.get_date(), "Start time", start_time)
    account.print_statement()
    return account.get_balance()





dl = DataLoader()
date_price_list = dl.load_data("../data/icici/")

# for start_time in range(50, 250):
profit = 0
loss = 0
for date_price in date_price_list:
    evaluate(Market(date_price), date_price.get_time_price_list()[50].get_time())


# profit = 0
# loss = 0
# for i in range(1, 365):
#     balance = evaluate(i)
#     diff = balance - 50000
#     if diff > 0:
#         profit += diff
#     else:
#         loss += diff
#
# print("Total Profit " + str(profit))
# print("Total loss " + str(loss))
# print("Net " + str(profit + loss))
