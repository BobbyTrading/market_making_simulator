import random
from trader_base import Trader
from order import Order


class DummyTrader(Trader):
    def __init__(self, id, seed=2023):
        random.seed(seed)
        super(DummyTrader, self).__init__()
        self.id = id
        self.num_orders = 4
    
    def place_order(self, exchange):
        market = exchange.market
        p = market.get_price
        tick_size = market.tick_size
        orders = []
        for _ in range(self.num_orders):
            type = ["BID", "ASK"][random.randint(0,1)]
            if type == "BID":
                o = p + random.randint(-3,2) * tick_size
            else:
                o = p + random.randint(-2,3) * tick_size
            v = random.randint(2,10)
            orders.append(Order(self.id, type, o, v))
        return orders
