class Order:
    def __init__(self, id, order_type, price, quantity):
        self.id = id
        self.type = order_type    # 'BID' or 'ASK'
        self.price = price
        self.quantity = quantity
