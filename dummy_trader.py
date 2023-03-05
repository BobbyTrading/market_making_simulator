import random
from trader_base import Trader
from order import Order


class DummyTrader(Trader):
    def __init__(self, id):
        super(DummyTrader, self).__init__()
        self.id = id
        self.num_orders = 4
    
    def place_order(self, exchange, *markets):
        market = markets[0]
        p = market.get_price
        tick_size = market.tick_size
        orders = []
        for _ in range(self.num_orders):
            o = p + random.randint(1,2) * [1,-1][random.randint(0,1)] * tick_size
            v = random.randint(2,10)
            type = ["BID", "ASK"][random.randint(0,1)]
            orders.append(Order(self.id, type, o, v))
        return orders
