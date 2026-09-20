import streamlit as st
import plotly.graph_objects as go
from engine.tick import run_simulation
from indicators import calculate_indicators
from validation import fetch_real_data, compare_returns_distribution

st.set_page_config(page_title="Market Simulation Dashboard", layout="wide")

st.title("Market Simulation: Order Book to Chart Patterns")

st.sidebar.header("Simulation Controls")
ticks = st.sidebar.slider("Number of Ticks", 100, 5000, 1000)
traders_per_tick = st.sidebar.slider("Traders per Tick", 1, 50, 10)
maker_ratio = st.sidebar.slider("Maker Ratio", 0.1, 0.9, 0.7)
max_deviation = st.sidebar.slider("Max Price Deviation %", 0.001, 0.05, 0.01)

if st.sidebar.button("Run Simulation"):
    with st.spinner("Simulating..."):
        df, _ = run_simulation(ticks, traders_per_tick, maker_ratio, max_deviation)
        df = calculate_indicators(df)
        st.session_state['sim_data'] = df

if 'sim_data' in st.session_state:
    df = st.session_state['sim_data']
    
    tab1, tab2 = st.tabs(["Candlestick Chart", "Validation Stats"])
    
    with tab1:
        st.subheader("Simulated Price Chart")
        fig = go.Figure(data=[go.Candlestick(x=df['tick'],
                        open=df['open'],
                        high=df['high'],
                        low=df['low'],
                        close=df['close'],
                        name='Price')])
                        
        fig.add_trace(go.Scatter(x=df['tick'], y=df['SMA_20'], line=dict(color='orange', width=1.5), name='SMA 20'))
        fig.add_trace(go.Scatter(x=df['tick'], y=df['SMA_50'], line=dict(color='blue', width=1.5), name='SMA 50'))
        
        fig.update_layout(xaxis_rangeslider_visible=False, height=600, template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
        
    with tab2:
        st.subheader("Validation vs Real Data (BTC-USD)")
        with st.spinner("Fetching real data for comparison..."):
            real_df = fetch_real_data("BTC-USD", "1mo", "1h")
            
        if not real_df.empty:
            stats = compare_returns_distribution(df, real_df)
            
            col1, col2 = st.columns(2)
            col1.metric("Simulated Volatility (Std Dev)", f"{stats['sim_std']:.4f}")
            col2.metric("Real Volatility (Std Dev)", f"{stats['real_std']:.4f}")
            
            col1.metric("Simulated Kurtosis", f"{stats['sim_kurtosis']:.2f}")
            col2.metric("Real Kurtosis", f"{stats['real_kurtosis']:.2f}")
            
            st.info("Notice how purely random traders with a high maker ratio can produce similar return fat-tails (kurtosis) as real markets!")
