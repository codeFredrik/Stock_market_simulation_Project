import random

class RandomTrader:
    def __init__(self, maker_ratio=0.5, max_deviation=0.01):
        self.maker_ratio = maker_ratio
        self.max_deviation = max_deviation
        
    def act(self, order_book):
        is_maker = random.random() < self.maker_ratio
        side = 'buy' if random.random() < 0.5 else 'sell'
        size = random.randint(1, 10)
        
        if is_maker:
            ref_price = order_book.last_price
            deviation = ref_price * self.max_deviation
            if side == 'buy':
                price = ref_price - random.uniform(0, deviation)
            else:
                price = ref_price + random.uniform(0, deviation)
            order_book.add_maker_order(side, round(price, 2), size)
            return None
        else:
            return order_book.execute_taker_order(side, size)
