import numpy as np
import json

class Market:
    def __init__(self, data):
        self.data = data
        self.time = -1

    def getTime(self):
        return self.time

    def tick(self):
        self.time = self.time + 1
        if (self.time >= len(self.data)):
            return False

    def getPrice(self):
        return self.data[self.time]

    def getLastPrice(self):
        return self.data[self.time - 1]


class Account:
    def __init__(self):
        self.balance = 0
        self.stock = 0
        self.lastPurchasePrice = -1
        self.lastSoldPrice = -1

    def depositAmount(self, amount):
        # print("Deposited Amount " + str(amount))
        self.balance = self.balance + amount
        # self.printStatement()

    def withdrawAmount(self, amount):
        if (amount > self.balance):
            raise Exception("Sorry, insufficient balance!!!")
            # print("withdrawAmount " + str(amount))
        self.balance = self.balance - amount
        # self.printStatement()

    def buyStock(self, stockPrice):
        # print("Buy Stock at " + str(stockPrice))
        self.stock = self.stock + (self.balance / stockPrice)
        self.balance = 0
        self.lastPurchasePrice = stockPrice
        # self.printStatement()

    def sellStock(self, stockPrice):
        # print("Sell Stock at " + str(stockPrice))
        self.balance = self.balance + (stockPrice * self.stock)
        self.stock = 0
        self.lastSoldPrice = stockPrice
        # self.printStatement()

    def printStatement(self):
        print("-------------")
        print("Bank Balance " + str(self.balance))
        print("Stocks " + str(self.stock))
        # print("Last purchase price " + str(self.lastPurchasePrice))
        # print("Last sold price " + str(self.lastSoldPrice))
        print("-------------")
        print("")

    def getBalance(self):
        return self.balance

    def getStock(self):
        return self.stock

    def getLastPurchasePrice(self):
        return self.lastPurchasePrice

    def getLastSoldPrice(self):
        return self.lastSoldPrice


def getStockData():
    with open('icici.json') as f:
        data = json.load(f)
    p = data['chart']['result'][0]['indicators']['quote'][0]['close']
    price = np.asarray(p)
    price = price[price.astype(bool)]
    price1 = price[10:]
    return price1.tolist()


def evaluate(startTime):
    market = Market(getStockData())
    account = Account()
    account.depositAmount(50000)

    while True:
        marketOpened = market.tick()
        if (marketOpened == False):
            break

        price = market.getPrice()
        lastPrice = market.getLastPrice();

        if (market.getTime() == startTime):
            # print("Purchasing stock at " + str(price))
            account.buyStock(price)
            continue

        if (market.getTime() > startTime):
            if account.getStock() > 0:
                diff = price - account.getLastPurchasePrice()
                if (diff <= -.1):
                    account.sellStock(price)
                elif (diff >= 4):
                    account.sellStock(price)
                    print("Purchase done!!!")
                    break
            else:
                diff = price - account.getLastPurchasePrice()
                if (diff >= 0):
                    account.buyStock(price)

    account.printStatement()
    return account.getBalance()


profit = 0
loss = 0
for i in range(1, 365):
    balance = evaluate(i)
    diff = balance - 50000
    if diff > 0:
        profit += diff
    else:
        loss += diff

print("Total Profit " + str(profit))
print("Total loss " + str(loss))
print("Net " + str(profit + loss))
