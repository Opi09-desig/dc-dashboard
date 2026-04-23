import streamlit as st
import pandas as pd

st.set_page_config(page_title="Eficiencia Energética", layout="wide")
st.title("⚡ Análisis Energético Global (2024)")
st.markdown("Basado en reportes del Uptime Institute y la IEA (Agencia Internacional de la Energía).")

# Métricas principales
col1, col2, col3 = st.columns(3)
col1.metric("PUE Promedio Global", "1.56", "-0.02 vs 2023")
col2.metric("Consumo DC Global (2024)", "415 TWh", "+36 TWh vs 2023")
col3.metric("Objetivo de PUE (Nuevos DC)", "1.30", "Óptimo")

st.markdown("---")

# Dos columnas para dos gráficas
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Evolución del PUE Global (2014-2024)")
    # Datos reales de tendencia de PUE
    pue_data = pd.DataFrame({
        "Año": ["2014", "2018", "2020", "2022", "2023", "2024"],
        "PUE Promedio": [1.70, 1.58, 1.59, 1.55, 1.58, 1.56]
    }).set_index("Año")
    st.line_chart(pue_data, color="#FF4B4B")
    st.caption("El estancamiento del PUE demuestra la dificultad de optimizar centros de datos legacy.")

with chart_col2:
    st.subheader("Proyección Consumo Global (TWh)")
    # Datos reales proyectados por la IEA
    energy_data = pd.DataFrame({
        "Año": ["2022", "2023", "2024", "2026 (Est)", "2030 (Est)"],
        "Consumo (TWh)": [340, 379, 415, 620, 945]
    }).set_index("Año")
    st.bar_chart(energy_data, color="#0068C9")
    st.caption("Crecimiento impulsado drásticamente por la adopción de IA Generativa.")