import streamlit as st
import pandas as pd

st.set_page_config(page_title="Impacto Financiero", layout="wide")
st.title("📈 Impacto Financiero y Riesgos Operativos")
st.markdown("Análisis de costos de inactividad (Downtime) y distribución de mercado en 2024.")

# Métrica de impacto crítico
st.error("⚠️ Costo promedio global por minuto de inactividad IT (Downtime) en 2024: **$14,056 USD**")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Causas Principales de Outages (2024)")
    st.write("Porcentaje de incidentes severos por categoría:")
    # Datos representativos de causas de caídas
    outage_causes = pd.DataFrame({
        "Causa": ["Energía (Power)", "Red (Network)", "Errores de TI / Software", "Refrigeración (Cooling)"],
        "Incidencia (%)": [43, 31, 14, 12]
    }).set_index("Causa")
    st.bar_chart(outage_causes, color="#FF8700")

with col2:
    st.subheader("Costo Acumulado por Caída (Simulador)")
    st.write("Costo proyectado si la infraestructura de red falla:")
    # Gráfica de área mostrando cómo se dispara el costo con el tiempo
    downtime_minutes = [0, 15, 30, 45, 60]
    cost_data = pd.DataFrame({
        "Minutos": downtime_minutes,
        "Pérdida (USD)": [0, 210840, 421680, 632520, 843360]
    }).set_index("Minutos")
    st.area_chart(cost_data, color="#29B09D")

st.info("💡 **Decisión Arquitectónica:** Al usar AWS ECS Fargate y un Load Balancer, mitigamos el riesgo del 43% de caídas causadas por problemas de energía física.")