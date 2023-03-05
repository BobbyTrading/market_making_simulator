class Trader:
    def __init__(self):
        self.pnl = []
        self.pos = 0
        self.cash = 0
        self.trading_fee = 0

    def place_order(self, exchange, *markets):
        raise NotImplementedError()
    
    def update_position(self, type, price, vol):
        if type == "BID":
            self.pos += vol
            self.cash -= price * vol + self.trading_fee * vol
        else:
            self.pos -= vol
            self.cash += price * vol - self.trading_fee * vol
        self.pnl += [self.pos * price + self.cash]
