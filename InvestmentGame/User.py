class User:
    def __init__(self, user_name, currency, balance):
        self.user_name = user_name
        self.currency = currency
        self.balance = balance
        self.orders = []
        self.portfolio = {}

    def __repr__(self):
        return self.user_name + "," + self.currency + "," + str(self.balance)

    def update_portfolio(self, symbol, number, ordertype):
        if ordertype == "buy":
                self.portfolio[symbol] += number

        elif ordertype == "sell":
                self.portfolio[symbol] -= number

        else:
            return "Order type is not known"

    def add_portfolio(self, symbol, number):
        self.portfolio[symbol] = number

    def update_orderlist(self, wantorder, order_id, ordertype, symbol, time, amount, price, value):
        if wantorder == "y":
            self.orders.append({"order_id":order_id,"order_type":ordertype, "symbol":symbol, "date":time, "amount":amount, "price":price, "value":value})
        else:
            return "ERROR"