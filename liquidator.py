import random
import math
from trader_base import Trader
from order import Order

class Liquidator(Trader):
    def __init__(self, id, intensity=1.0, seed=2023):
        random.seed(seed)
        self.intensity = intensity
        super(Liquidator, self).__init__()
        self.id = id
        self.num_orders = 4
    
    def place_order(self, exchange):
        # intensity of making orders
        u = random.random()
        if u > 1.0 - math.exp(-self.intensity):
            return []
        type = ["BID", "ASK"][random.randint(0, 1)]
        orders = exchange.orders
        if type == "BID":
            asks = [order for order in orders if order.type == "ASK"]
            if len(asks) == 0:
                return []
            asks.sort(key=lambda o: o.price, reverse=False)
            o = asks[0].price
            v = asks[0].quantity
            return [Order(self.id, type, o, v)]
        else:
            asks = [order for order in orders if order.type == "BID"]
            if len(asks) == 0:
                return []
            asks.sort(key=lambda o: o.price, reverse=True)
            o = asks[0].price
            v = asks[0].quantity
            return [Order(self.id, type, o, v)]
        return orders
