import random


class Exchange:
    def __init__(self, market):
        self.players = {}
        self.orders = []
        self.market = market
    
    def reset(self):
        self.orders = []
    
    def register_player(self, player):
        self.players[player.id] = player
    
    def receive_orders(self, orders):
        self.orders += orders

    def match_order_pair(self, order1, order2):
        price = [order1.price, order2.price][random.randint(0,1)]
        vol = min(order1.quantity, order2.quantity)
        player1 = self.players[order1.id]
        player2 = self.players[order2.id]
        self.transact(player1, order1.type, price, vol)
        self.transact(player2, order2.type, price, vol)

    def transact(self, player, type, price, vol):
        player.update_position(type, price, vol)
        # print(f"{type} {vol} for {price}; pnl: {self.pnl[-1]:.2f}; pos: {self.pos}")

    def match_orders(self):
        bids = [order for order in self.orders if order.type == "BID"]
        asks = [order for order in self.orders if order.type == "ASK"]
        bids.sort(key=lambda o: (o.price, random.random()), reverse=True)
        asks.sort(key=lambda o: (o.price, random.random()), reverse=False)

        removed_bids = []
        removed_asks = []

        for i, bid in enumerate(bids):
            for j, ask in enumerate(asks):
                if j in removed_asks:
                    continue
                if ask.price <= bid.price:
                    removed_bids.append(i)
                    removed_asks.append(j)
                    self.match_order_pair(bid, ask)
                    break
        self.orders = []
        for i in range(len(bids)):
            if i not in removed_bids:
                self.orders.append(bids[i])
        for j in range(len(asks)):
            if j not in removed_asks:
                self.orders.append(asks[j])