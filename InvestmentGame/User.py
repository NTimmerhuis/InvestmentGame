class User:
    def _init_(self, user_name, currency, balance):
        self.user_name = user_name
        self.currency = currency
        self.balance = balance
        self.orders = []
