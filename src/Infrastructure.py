class DayMarket:
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

    def get_market_close_price(self):
        return self.time_price_list[-1].get_price()


class Account:
    def __init__(self):
        self.balance = 0
        self.stock = 0
        self.lastPurchasePrice = -1
        self.lastSoldPrice = -1

    def deposit_amount(self, amount):
        self.balance = self.balance + amount

    def withdraw_amount(self, amount):
        if amount > self.balance:
            raise Exception("Sorry, insufficient balance!!!")
        self.balance = self.balance - amount

    def buy_stock(self, stockPrice):
        if self.balance > 0:
            self.stock = self.stock + (self.balance / stockPrice)
            self.balance = 0
            self.lastPurchasePrice = stockPrice

    def sell_stock(self, stockPrice):
        if stockPrice is None:
            raise Exception
        if self.stock > 0:
            self.balance = self.balance + (stockPrice * self.stock)
            self.stock = 0
            self.lastSoldPrice = stockPrice

    def print_statement(self):
        print("-------------")
        print("Bank Balance " + str(self.balance))
        print("Stocks " + str(self.stock))
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

