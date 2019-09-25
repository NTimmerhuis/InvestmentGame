class User:
    def __init__(self, user_name, currency, balance):
        self.user_name = user_name
        self.currency = currency
        self.balance = balance
        self.orders = []

    def __repr__(self):
        return str(self.user_name + "," + self.currency + "," +  self.balance + "," + self.orders)

