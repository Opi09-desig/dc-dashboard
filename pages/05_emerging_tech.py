import streamlit as st
import pandas as pd

st.set_page_config(page_title="Tecnologías Emergentes", layout="wide")
st.title(" Roadmap de Tecnologías Emergentes")
st.markdown("Evaluación de impacto, viabilidad y Retorno de Inversión (ROI) para la modernización de la infraestructura.")

st.markdown("---")

# Tres columnas tipo "Tarjetas"
col1, col2, col3 = st.columns(3)

with col1:
    st.info("💧 **Liquid Cooling (Enfriamiento Líquido)**")
    st.metric("Impacto proyectado en PUE", "-15%", "Alta Viabilidad")
    st.write("Enfriamiento directo al chip necesario para soportar racks de Inteligencia Artificial de alta densidad (>30kW).")

with col2:
    st.warning("🧠 **AI Ops (Mantenimiento Predictivo)**")
    st.metric("Reducción de Fallas Físicas", "40%", "En Fase Piloto")
    st.write("Uso de modelos de Machine Learning (Deep Learning) para predecir fallas en hardware antes de que causen Downtime.")

with col3:
    st.success("🌐 **Edge Computing**")
    st.metric("Mejora en Latencia", "-25ms", "Fase de Evaluación")
    st.write("Despliegue de micro-nodos de datos cerca del usuario final para soportar aplicaciones de Internet de las Cosas (IoT).")

st.markdown("---")

# Gráfica de área para proyección financiera
st.subheader("Proyección de Ahorro Acumulado (Próximos 5 años)")
st.write("Impacto financiero estimado tras implementar el Roadmap Tecnológico completo:")

ahorro_data = pd.DataFrame({
    "Año": ["2024", "2025", "2026", "2027", "2028"],
    "Ahorro Operativo (USD)": [50000, 125000, 210000, 340000, 520000]
}).set_index("Año")

st.area_chart(ahorro_data, color="#00C853")