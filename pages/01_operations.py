import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from faker import Faker

# Configuración de página
st.set_page_config(page_title="AWS QRO-1 | Operations", layout="wide")
fake = Faker()

# --- CSS PERSONALIZADO PARA LOOK PROFESIONAL ---
st.markdown(
    """
    <style>
    /* Estilo para el contenedor principal de la métrica (la tarjeta) */
    [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {
        background-color: #1E1E1E !important; /* Fondo gris oscuro */
        border-radius: 10px !important;       /* Bordes redondeados */
        padding: 15px !important;            /* Espaciado interno */
        box-shadow: 0 4px 6px rgba(0,0,0,0.3) !important; /* Sombra sutil */
    }

    /* Estilo específico para el valor principal (ej. 99.998%) */
    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;          /* Texto Blanco */
        font-size: 2.5rem !important;      /* Tamaño grande */
        font-weight: bold !important;       /* Negrita */
    }

    /* Estilo específico para la etiqueta superior (ej. Uptime SLA) */
    [data-testid="stMetricLabel"] p {
        color: #AAAAAA !important;          /* Texto gris claro */
        font-size: 1rem !important;        /* Tamaño normal */
        margin-bottom: 0px !important;      /* Quitar margen inferior */
    }
    
    /* Estilo para las flechas de delta (verde/rojo) */
    [data-testid="stMetricDelta"] {
        color: inherit !important;          /* Mantener color verde/rojo original */
        background-color: transparent !important; /* Quitar fondo de la flecha */
        box-shadow: none !important;        /* Quitar sombra de la flecha */
    }
    </style>
    """,
    unsafe_allow_html=True
)



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