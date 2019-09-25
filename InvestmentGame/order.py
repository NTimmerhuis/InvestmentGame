class Order:
    def __init__(self, order_id, time, amount, symbol, status, order_type, price, value):
        self.order_id = order_id
        self.time = time
        self.amount = amount
        self.symbol = symbol
        self.status = status
        self.order_type = order_type
        self.price = price
        self.value = value

    def __repr__(self):
        return str(self.order_id) + "," + self.time + "," + str(self.amount) + "," + self.status + self.order_type + "," + str(self.price) + "," + str(self.value)

    def total_order_value(self):
        totalordervalue = self.amount * self.price
        return totalordervalue







