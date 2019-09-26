class User:
    def __init__(self, user_name, currency, balance):
        self.user_name = user_name
        self.currency = currency
        self.balance = balance
        self.orders = []
        self.portfolio = {}

    def __repr__(self):
        return self.user_name + "," + self.currency + "," + str(self.balance)

    def update_portfolio(self, symbol, number):
        self.portfolio[symbol] = number
