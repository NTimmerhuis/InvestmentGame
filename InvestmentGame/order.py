class Order:
    order_id = 0
    def __init__(self, time, price, amount, fund_name, status, order_type):
        self.order_id = Order.order_id
        self.time = time
        self.price = price
        self.amount = amount
        self.fund_name = fund_name
        self.status = status
        self.order_type = order_type
        Order.order_id += 1

    def total_order_value(self):
        totalordervalue = self.amount * self.price
        return totalordervalue







