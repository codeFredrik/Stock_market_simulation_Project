import pandas as pd
import pandas_ta as ta

def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Takes an OHLCV DataFrame, calculates standard technical indicators,
    and returns the dataframe with the new indicator columns.
    """
    df = df.copy()
    
    # Simple Moving Averages
    df.ta.sma(length=20, append=True)
    df.ta.sma(length=50, append=True)
    
    # MACD (Moving Average Convergence Divergence)
    df.ta.macd(fast=12, slow=26, signal=9, append=True)
    
    # RSI (Relative Strength Index)
    df.ta.rsi(length=14, append=True)
    
    # Bollinger Bands
    df.ta.bbands(length=20, append=True)
    
    return df
