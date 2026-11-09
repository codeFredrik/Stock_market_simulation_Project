# Market Simulation Project

A Python-based market simulation that replicates how real chart patterns emerge from pure order book mechanics (no psychology, no hand-coded patterns).

## Architecture

- **Simulation Engine (`engine/`)**: Custom limit order book using Python's `heapq`. Random traders split into Makers (limit orders) and Takers (market orders).
- **Indicators (`indicators.py`)**: `pandas-ta` wrapper to compute standard technical indicators (SMA, MACD, RSI, Bollinger Bands).
- **Validation (`validation.py`)**: `yfinance` integration to compare statistical properties (volatility, skew, kurtosis) of simulated returns against real market data.
- **Dashboard (`app.py`)**: An interactive `streamlit` dashboard with `plotly` candlestick visualization and controls.

## Project Structure

```text
Stock_market_simluation_Project/
├── .gitattributes             # Git line-ending normalization
├── .gitignore                 # Python, venv, and IDE ignore rules
├── README.md                  # Project overview and run guide
├── requirements.txt           # Project dependencies
├── app.py                     # Streamlit web dashboard
├── indicators.py              # Indicator calculations
├── validation.py              # Real market data fetching and statistical checks
├── engine/                    # Core simulation package
│   ├── __init__.py            # Package exports
│   ├── orderbook.py           # Limit order book matching logic
│   ├── tick.py                # Tick runner and OHLCV aggregation
│   └── trader.py              # Maker and Taker random trader agents
├── notebooks/                 # Interactive Jupyter notebooks
│   ├── core_simulation.ipynb  # Step-by-step modular walkthrough
│   └── exploration.ipynb      # Deep-dive math proofs and order depth heatmap
└── docs/                      # Documentation
    └── market_sim_aim.md      # Detailed project vision and specifications
```

## How to Run

1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   # Windows PowerShell
   .\.venv\Scripts\Activate.ps1
   # macOS/Linux
   source .venv/bin/activate
   ```

2. Install the required dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```

3. Run the Streamlit dashboard:
   ```bash
   streamlit run app.py
   ```

The validation tab downloads recent BTC-USD data from Yahoo Finance at runtime. That comparison requires network access; the core simulation itself runs offline.
