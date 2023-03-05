import random


class Market:
    def __init__(self, price_stream, tick_size=1.0):
        self.tick_size = tick_size
        self.price_stream = price_stream
        self.t = 0

    @property
    def is_end(self):
        return self.t >= len(self.price_stream)

    @property
    def get_price(self):
        return self.price_stream[self.t]

    @property
    def get_next_price(self):
        if self.t + 1 < len(self.price_stream):
            return self.price_stream[self.t + 1]
        else:
            return None

    def tick(self):
        self.t += 1

    def reset(self):
        self.t = 0
