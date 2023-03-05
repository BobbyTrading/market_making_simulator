from trader_base import Trader
from order import Order

class MarketMaker(Trader):
    def __init__(self, id, max_inventory, trading_fee):
        super(MarketMaker, self).__init__()
        self.max_inventory = max_inventory
        self.trading_fee = trading_fee
        self.id = id
    
    def place_order(self, exchange, *markets):
        market = markets[0]
        p = market.get_price
        price_tick = market.tick_size
        orders = exchange.orders
        offers = []
        bids = [(item.price, item.quantity) for item in orders if item.type == "BID" and item.price < p]
        asks = [(item.price, item.quantity) for item in orders if item.type == "ASK" and item.price > p]
        bids.sort(reverse=True)
        asks.sort(reverse=False)

        if len(bids) == 0 and len(asks) == 0:
            if self.max_inventory > self.pos:
                o1 = Order(self.id, "BID", p - 2 * price_tick, self.max_inventory - self.pos)
                offers.append(o1)
            if self.max_inventory > -self.pos:
                o2 = Order(self.id, "ASK", p + 2 * price_tick, self.max_inventory + self.pos)
                offers.append(o2)
        elif len(bids) > 0 and len(asks) == 0:
            if self.max_inventory > self.pos:
                o1 = Order(self.id, "BID", bids[0][0] + price_tick, self.max_inventory - self.pos)
                offers.append(o1)
            if self.max_inventory > -self.pos:
                o2 = Order(self.id, "ASK", bids[0][0] + 4 * price_tick, self.max_inventory + self.pos)
                offers.append(o2)
        elif len(bids) == 0 and len(asks) > 0:
            if self.max_inventory > self.pos:
                o1 = Order(self.id, "BID", asks[0][0] - 4 * price_tick, self.max_inventory - self.pos)
                offers.append(o1)
            if self.max_inventory > -self.pos:
                o2 = Order(self.id, "ASK", asks[0][0] - price_tick, self.max_inventory + self.pos)
                offers.append(o2)
        elif asks[0][0] - bids[0][0] >= 2 * price_tick:
            if self.max_inventory > self.pos:
                o1 = Order(self.id, "BID", bids[0][0] + (0 if self.pos > 0 else 1) * price_tick, self.max_inventory - self.pos)
                offers.append(o1)
            if self.max_inventory > -self.pos:
                o2 = Order(self.id, "ASK", asks[0][0] + (0 if self.pos < 0 else -1) * price_tick, self.max_inventory + self.pos)
                offers.append(o2)
        return offers
