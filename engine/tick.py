import pandas as pd
import random
from engine.orderbook import OrderBook
from engine.trader import RandomTrader

def run_simulation(ticks=1000, traders_per_tick=10, maker_ratio=0.7, max_deviation=0.02):
    order_book = OrderBook()
    traders = [RandomTrader(maker_ratio=maker_ratio, max_deviation=max_deviation) for _ in range(50)]
    
    # Pre-seed liquidity
    for _ in range(100):
        random.choice(traders).act(order_book)
        
    price_history = []
    
    for tick in range(ticks):
        tick_prices = []
        for _ in range(traders_per_tick):
            trader = random.choice(traders)
            exec_price = trader.act(order_book)
            if exec_price is not None:
                tick_prices.append(exec_price)
                
        if not tick_prices:
            tick_prices = [order_book.last_price]
            
        price_history.append({
            'tick': tick,
            'open': tick_prices[0],
            'high': max(tick_prices),
            'low': min(tick_prices),
            'close': tick_prices[-1],
            'volume': len(tick_prices)
        })
        
    df = pd.DataFrame(price_history)
    return df, order_book
