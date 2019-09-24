class Order:
    def __init__(self, order_id, price, amount, order_type, fund_name, status):
        self.order_id = order_id
        self.price = price
        self.amount = amount
        self.order_type = order_type
        self.fund_name = fund_name
        self.status = status

    def total_order_value(self, amount, price):
        self.amount * self.price = total_order_value
        return total_order_value

