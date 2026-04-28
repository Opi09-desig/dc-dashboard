import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AWS QRO-1 | Energy Efficiency", layout="wide")

# --- CSS PARA IDENTIDAD VISUAL ---
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

st.title(" Energy Management & Sustainability")
st.subheader("AWS Mexico Central Region | Sustainability Targets")

# --- MÉTRICAS PRINCIPALES ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Current PUE (QRO-1)", "1.18", "-0.05", help="Power Usage Effectiveness")
with col2:
    st.metric("Renewable Energy Mix", "85%", "+12%")
with col3:
    st.metric("Water Usage Effectiveness", "0.25 L/kWh", "Optimal")

st.divider()

# --- CALCULADORA INTERACTIVA DE PUE (Requisito Guía) ---
with st.expander("🧮 Interactive PUE Calculator"):
    st.write("Calculate the efficiency of your specific data center row or hall.")
    it_load = st.number_input("IT Equipment Load (kW)", min_value=1.0, value=100.0)
    cooling_load = st.number_input("Cooling & Lighting Load (kW)", min_value=1.0, value=20.0)
    
    total_facility = it_load + cooling_load
    calculated_pue = total_facility / it_load
    
    st.markdown(f"### Resulting PUE: **{calculated_pue:.2f}**")
    st.latex(r"PUE = \frac{\text{Total Facility Power}}{\text{IT Equipment Power}}")

# --- GRÁFICAS PROFESIONALES CON PLOTLY ---
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("PUE Trend: Global vs. AWS QRO-1")
    pue_trend = pd.DataFrame({
        "Year": ["2022", "2023", "2024", "2025 (Proj)"],
        "Global Avg": [1.55, 1.58, 1.56, 1.54],
        "AWS QRO-1": [1.22, 1.20, 1.18, 1.15]
    })
    
    # Cambiamos "#gray" por "gray" (nombre de CSS) o un Hex real como "#808080"
    fig_pue = px.line(pue_trend, x="Year", y=["Global Avg", "AWS QRO-1"], 
                      markers=True, 
                      template="plotly_dark", 
                      color_discrete_sequence=["gray", "#c9a84c"]) # <--- FIX AQUÍ
    
    fig_pue.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_pue, use_container_width=True)

with chart_col2:
    st.subheader("Projected Consumption (TWh)")
    energy_data = pd.DataFrame({
        "Year": ["2022", "2023", "2024", "2026 (Est)", "2030 (Est)"],
        "Consumption": [340, 379, 415, 620, 945]
    })
    fig_energy = px.bar(energy_data, x="Year", y="Consumption", 
                        template="plotly_dark", color_discrete_sequence=["#4a1a6e"])
    st.plotly_chart(fig_energy, use_container_width=True)