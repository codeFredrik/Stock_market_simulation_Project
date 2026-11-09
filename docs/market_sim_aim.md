# Market Simulation — Project Vision

## What We're Building

A Python-based market simulation that replicates how real chart patterns emerge from pure order book mechanics (no psychology, no hand-coded patterns). On top of the simulation engine, a live dashboard with real technical indicators and a validation layer that checks whether the sim's emergent patterns statistically match real market data.

This is simultaneously a math/stats project, a systems project, and a tradeable research tool.

---

## Core Thesis (from the video)

Patterns are not psychology. They are order book density artifacts. If we simulate a market with purely random traders and the right maker/taker ratio, support and resistance emerge from math alone. Our job is to:

1. Reproduce this mechanically
2. Quantify it with real indicators
3. Validate it against actual price data

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    SIMULATION ENGINE                │
│  OrderBook → TraderAgents → TickEngine → PriceLog  │
└───────────────────────┬─────────────────────────────┘
                        │ OHLCV stream
┌───────────────────────▼─────────────────────────────┐
│                  INDICATOR LAYER                    │
│     SMA / EMA / MACD / RSI / Bollinger Bands        │
└───────────────────────┬─────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────┐
│                  VALIDATION LAYER                   │
│   Sim patterns vs. real OHLCV (yfinance / CSV)      │
│   Statistical tests: pattern frequency, S/R density │
└───────────────────────┬─────────────────────────────┘
                        │
┌───────────────────────▼─────────────────────────────┐
│                    DASHBOARD (Streamlit)             │
│   Candlestick chart + Indicators + Order Book Heatmap│
└─────────────────────────────────────────────────────┘
```

---

## Phases

### Phase 1 — Simulation Engine
- `OrderBook` class: bid/ask sides as sorted heaps, maker placement, taker matching
- `Trader` base class → `RandomTrader` subclass (±1% price deviation, 50/50 maker-taker split)
- `TickEngine`: runs N ticks, records price history as OHLCV
- Reproduce the key mechanic: reduce makers → price begins to move → patterns emerge

**Output:** A clean price series that visually resembles a real chart

---

### Phase 2 — Indicator Layer
Compute standard indicators on the sim's OHLCV output using `pandas-ta`:

| Indicator | Purpose |
|---|---|
| SMA 20 / 50 | Trend baseline |
| EMA 12 / 26 | MACD components |
| MACD + Signal | Momentum |
| RSI (14) | Overbought/oversold |
| Bollinger Bands | Volatility envelope |
| Volume Profile | Order density by price level |

**Output:** Indicator time series appended to the OHLCV dataframe

---

### Phase 3 — Validation Layer
The most DS-heavy part. Two approaches:

**A. Visual comparison**
- Pull real OHLCV for a liquid instrument (e.g. BTC-USD or NIFTY 50) via `yfinance`
- Run same indicators on both
- Overlay or side-by-side plot: does the sim produce similar indicator distributions?

**B. Statistical validation**
- Support/Resistance level detection: find local minima/maxima, measure how often price respects them
- Compare S/R "hit rate" in sim vs. real data
- Autocorrelation of price level revisits
- Optional: KS test or distribution comparison on returns

**Output:** A validation report / notebook section with concrete stats

---

### Phase 4 — Dashboard (Streamlit)
Interactive UI with:

- **Controls panel:** number of traders, maker ratio, tick count, price drift %, random seed
- **Candlestick chart:** plotly, with indicator overlays toggleable
- **Order book heatmap:** price level vs. time, color = order density (reproduces the video's visualization)
- **Validation tab:** sim vs. real data comparison
- **Run button:** re-runs simulation live in the browser

---

## Stack

| Component | Library |
|---|---|
| Simulation engine | Pure Python (heapq, dataclasses) |
| Data manipulation | pandas, numpy |
| Indicators | pandas-ta |
| Real market data | yfinance |
| Charts | plotly |
| Dashboard | Streamlit |
| Optional GPU speedup | numba (later) |

---

## Deliverables

1. `engine/` — order book + trader + tick engine (importable module)
2. `indicators.py` — wraps pandas-ta, takes OHLCV → returns indicator df
3. `validation.py` — fetches real data, runs comparisons, outputs stats
4. `app.py` — Streamlit dashboard
5. `notebooks/exploration.ipynb` — scratchpad for the stats/validation work
6. `README.md` — project summary suitable for GitHub portfolio

---

## Portfolio Value

- Demonstrates **stochastic modeling** (random processes, order book dynamics)
- Demonstrates **time series analysis** (indicators, autocorrelation, S/R detection)
- Demonstrates **statistical validation** (not just "it looks similar" — actual tests)
- Demonstrates **end-to-end product thinking** (sim → analysis → interactive UI)
- Strong talking point: *"I reproduced emergent market patterns from first principles and validated them statistically against real data"*

---

## Out of Scope (for now)

- RL/AI trading agent (natural Phase 5 if this goes well)
- Real-time data feed integration
- Multiple asset simulation
- Backtesting framework
