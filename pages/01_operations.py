import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from faker import Faker

# Configuración de página
st.set_page_config(page_title="AWS QRO-1 | Operations", layout="wide")
fake = Faker()

# --- CSS PERSONALIZADO PARA LOOK PROFESIONAL ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 10px; }
    .status-card { border-left: 5px solid #00ff00; padding: 10px; background: #161b22; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🌐 AWS Mexico Central (mx-central-1)")
st.subheader("Availability Zone: QRO-1 | Operations Management")

# --- UNIDAD 3: MÉTRICAS DE OPERACIÓN (SLA) ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Uptime SLA (Monthly)", value="99.998%", delta="0.001%")
with col2:
    st.metric(label="Active Incidents", value="2", delta="-1", delta_color="normal")
with col3:
    st.metric(label="Pending MACs", value="14", delta="3")
with col4:
    st.metric(label="Avg Response Time", value="4.2ms", delta="-0.5ms")

st.divider()

# --- INTERACTIVE GAUGE (Uptime) ---
fig_uptime = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 99.998,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Critical Systems Health"},
    gauge = {
        'axis': {'range': [99, 100]},
        'bar': {'color': "#c9a84c"},
        'steps': [
            {'range': [99, 99.9], 'color': "gray"},
            {'range': [99.9, 100], 'color': "black"}],
        'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 99.99}
    }
))
fig_uptime.update_layout(paper_bgcolor='rgba(0,0,0,0)', font={'color': "white"})
st.plotly_chart(fig_uptime, use_container_width=True)

# --- TABLA DE PROCESOS MAC (Moves, Adds, Changes) ---
st.subheader("📋 Recent MAC Activity (Unit 3)")
mac_data = {
    "ID": [f"MAC-{i}" for i in range(1001, 1006)],
    "Type": ["Rack Install", "Fiber Cross-Connect", "Server Decommission", "UPS Maintenance", "PDU Swap"],
    "Technician": [fake.name() for _ in range(5)],
    "Status": ["In Progress", "Completed", "Pending", "Completed", "Scheduled"],
    "Priority": ["High", "Medium", "Critical", "Low", "High"]
}
df_mac = pd.DataFrame(mac_data)
st.dataframe(df_mac, use_container_width=True)