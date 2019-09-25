class User:
    def __init__(self, user_name, currency, balance):
        self.user_name = user_name
        self.currency = currency
        self.balance = balance
        self.orders = []

    def __repr__(self):
        return self.user_name + "," + self.currency + "," + str(self.balance)

