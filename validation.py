import yfinance as yf
import pandas as pd
import numpy as np

def fetch_real_data(ticker="BTC-USD", period="1mo", interval="1h"):
    """
    Fetches real OHLCV data from Yahoo Finance.
    """
    data = yf.download(ticker, period=period, interval=interval)
    if not data.empty:
        # Standardize column names to lowercase
        data = data.reset_index()
        # Flatten MultiIndex columns if present
        if isinstance(data.columns, pd.MultiIndex):
            data.columns = [col[0].lower() for col in data.columns]
        else:
            data.columns = [col.lower() for col in data.columns]
    return data

def compare_returns_distribution(df_sim, df_real):
    """
    Compares the return distributions of simulated vs real data.
    """
    sim_returns = df_sim['close'].pct_change().dropna()
    real_returns = df_real['close'].pct_change().dropna()
    
    stats = {
        'sim_mean': float(sim_returns.mean()),
        'real_mean': float(real_returns.mean()),
        'sim_std': float(sim_returns.std()),
        'real_std': float(real_returns.std()),
        'sim_skew': float(sim_returns.skew()),
        'real_skew': float(real_returns.skew()),
        'sim_kurtosis': float(sim_returns.kurtosis()),
        'real_kurtosis': float(real_returns.kurtosis())
    }
    return stats
