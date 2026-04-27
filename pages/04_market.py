import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AWS QRO-1 | Market Intelligence", layout="wide")

# --- CSS PARA IDENTIDAD VISUAL (AWS GOLD) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #c9a84c; padding: 15px; border-radius: 10px; }
    .stAlert { background-color: #161b22; border: 1px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

st.title(" Market Intelligence & Financial Impact")
st.subheader("Mexico Central Region (Querétaro) | Hyperscale Analysis")

# --- MÉTRICAS DE INVERSIÓN (DATOS REALES) ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("AWS Investment (MX)", "$5.0B USD", "Next 15 Years")
with col2:
    st.metric("Azure Investment (MX)", "$1.3B USD", "Announced 2024")
with col3:
    st.metric("Estimated Local Jobs", "6,500+", "Direct/Indirect")

st.divider()

# --- COMPARATIVA DE MERCADO ---
col_map, col_chart = st.columns([1, 1])

with col_map:
    st.subheader("📍 Mexico DC Hotspots")
    # Simulación de hubs principales
    hubs_data = pd.DataFrame({
        "City": ["Querétaro", "CDMX", "Monterrey", "Guadalajara"],
        "DC Count": [15, 8, 5, 3],
        "Capacity (MW)": [300, 120, 80, 45]
    })
    fig_hubs = px.bar(hubs_data, x="City", y="Capacity (MW)", 
                      title="Installed Capacity by Region",
                      template="plotly_dark", color_discrete_sequence=["#c9a84c"])
    st.plotly_chart(fig_hubs, use_container_width=True)

with col_chart:
    st.subheader("📉 The Cost of Failure")
    st.error("Average Downtime Cost: **$14,056 USD/min**")
    
    # Simulador de pérdida acumulada
    mins = [0, 15, 30, 45, 60]
    loss = [m * 14056 for m in mins]
    fig_loss = px.area(x=mins, y=loss, title="Cumulative Financial Loss (Downtime)",
                       labels={'x':'Minutes', 'y':'Loss (USD)'},
                       template="plotly_dark", color_discrete_sequence=["#ff4b4b"])
    st.plotly_chart(fig_loss, use_container_width=True)

# --- UNIDAD 4: ESTRATEGIA ---
st.subheader(" Strategic Competitive Analysis")
st.info("""
**Market Strategy:** Querétaro has become the "Silicon Valley" of Mexico due to its low seismic activity and energy connectivity. 
By deploying on **AWS ECS Fargate**, our architecture avoids the high CAPEX of physical maintenance while gaining the resilience of a $5B USD infrastructure.
""")