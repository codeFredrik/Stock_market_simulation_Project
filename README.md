# Market Simulation Project

A Python-based market simulation that replicates how real chart patterns emerge from pure order book mechanics (no psychology, no hand-coded patterns).

## Architecture

- **Simulation Engine**: Custom limit order book using Python's `heapq`. Random traders split into Makers (limit orders) and Takers (market orders).
- **Indicators**: `pandas-ta` to compute standard technical indicators.
- **Validation**: `yfinance` to compare the statistical properties of the simulated returns against real market data.
- **Dashboard**: A fully interactive `streamlit` dashboard with `plotly` visualizations.

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

The validation tab downloads recent BTC-USD data from Yahoo Finance at runtime.
That comparison requires network access; the simulation itself runs offline.
