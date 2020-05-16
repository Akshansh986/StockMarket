class TimePrice:
    def __init__(self, time, price):
        self.time = time
        self.price = price

    def get_time(self):
        return self.time

    def get_price(self):
        return self.price


class DatePrice:

    def __init__(self, date, time_price_list):
        self.date = date
        self.time_price_list = time_price_list

    def get_date(self):
        return self.date

    def get_time_price_list(self):
        return self.time_price_list

    def set_time_price_list(self, time_price_list):
        self.time_price_list = time_price_list
