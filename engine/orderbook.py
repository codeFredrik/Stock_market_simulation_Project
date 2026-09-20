import heapq

class OrderBook:
    def __init__(self):
        self.bids = []  # Max-heap: (-price, size, order_id)
        self.asks = []  # Min-heap: (price, size, order_id)
        self.order_id_counter = 0
        self.last_price = 100.0
        
    def add_maker_order(self, side, price, size):
        self.order_id_counter += 1
        if side == 'buy':
            heapq.heappush(self.bids, (-price, size, self.order_id_counter))
        else:
            heapq.heappush(self.asks, (price, size, self.order_id_counter))
            
    def execute_taker_order(self, side, size):
        executed_value = 0.0
        executed_size = 0
        
        if side == 'buy':
            while size > 0 and self.asks:
                best_ask_price, ask_size, order_id = self.asks[0]
                if size >= ask_size:
                    heapq.heappop(self.asks)
                    executed_size += ask_size
                    executed_value += best_ask_price * ask_size
                    size -= ask_size
                    self.last_price = best_ask_price
                else:
                    self.asks[0] = (best_ask_price, ask_size - size, order_id)
                    executed_size += size
                    executed_value += best_ask_price * size
                    self.last_price = best_ask_price
                    size = 0
        else:
            while size > 0 and self.bids:
                neg_best_bid_price, bid_size, order_id = self.bids[0]
                best_bid_price = -neg_best_bid_price
                if size >= bid_size:
                    heapq.heappop(self.bids)
                    executed_size += bid_size
                    executed_value += best_bid_price * bid_size
                    size -= bid_size
                    self.last_price = best_bid_price
                else:
                    self.bids[0] = (neg_best_bid_price, bid_size - size, order_id)
                    executed_size += size
                    executed_value += best_bid_price * size
                    self.last_price = best_bid_price
                    size = 0
                    
        return (executed_value / executed_size) if executed_size > 0 else self.last_price
