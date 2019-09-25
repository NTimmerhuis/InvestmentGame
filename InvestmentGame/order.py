class Order:
    order_id = 0
    def __init__(self, order_id, time, price, amount, fund_name, status, order_type):
        self.order_id = order_id
        self.time = time
        self.price = price
        self.amount = amount
        self.fund_name = fund_name
        self.status = status
        self.order_type = order_type


    def total_order_value(self):
        totalordervalue = self.amount * self.price
        return totalordervalue







