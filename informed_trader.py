import random
from trader_base import Trader
from order import Order


class InformedTrader(Trader):
    def __init__(self, id, seed=2023):
        random.seed(seed)
        super(InformedTrader, self).__init__()
        self.id = id
    
    def place_order(self, exchange):
        market = exchange.market
        p = market.get_price
        p_next = market.get_next_price
        price_tick = market.tick_size
        if not p_next:
            return []
        if p_next > p:
            # place bid
            o = p_next - price_tick
            v = random.randint(5,10)
            type = "BID"
            return [Order(self.id, type, o, v)]
        else:
            # place bid
            o = p_next + price_tick
            v = random.randint(5,10)
            type = "ASK"
            return [Order(self.id, type, o, v)]
