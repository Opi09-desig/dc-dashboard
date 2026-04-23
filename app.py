import streamlit as st

st.set_page_config(page_title="Data Center Strategy", layout="wide")

# Banner con color inyectado vía HTML
st.markdown("""
<div style="background: linear-gradient(to right, #1e3c72, #2a5298); padding: 25px; border-radius: 10px; color: white; text-align: center; margin-bottom: 25px;">
    <h1 style="margin:0; color: white;">🌐 Data Center Operations Strategy</h1>
    <p style="margin:0; font-size: 18px;">Centro de Comando, Análisis de Mercado y Telemetría en Tiempo Real</p>
</div>
""", unsafe_allow_html=True)

# Métricas rápidas de bienvenida con impacto visual
col1, col2, col3 = st.columns(3)
col1.metric("Disponibilidad Objetivo", "99.99%", "Certificación Tier III")
col2.metric("Eficiencia Energética (PUE)", "1.20", "-0.05 optimización", delta_color="inverse")
col3.metric("Seguridad Operativa", "Nivel Óptimo", "ISO 27001 Activa")

st.markdown("---")

# Contexto de la arquitectura
col_text, col_tech = st.columns([2, 1])

with col_text:
    st.subheader("Enfoque Estratégico de la Infraestructura")
    st.write("""
    Este sistema centraliza la gestión operativa y el análisis del centro de datos desplegado en la nube.
    * **Resiliencia:** Mitigación de Downtime mediante balanceadores de carga.
    * **Sostenibilidad:** Monitoreo constante del PUE y consumo energético.
    * **Innovación:** Adopción de IA para mantenimiento predictivo.
    """)

with col_tech:
    st.info("**Stack Tecnológico**")
    st.write("- **Frontend:** Streamlit")
    st.write("- **Deploy:** Docker & AWS Fargate")
    st.write("- **IaC:** Terraform")
    st.write("- **CI/CD:** GitHub Actions")