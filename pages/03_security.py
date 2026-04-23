import streamlit as st
import pandas as pd

st.set_page_config(page_title="Seguridad y Auditoría", layout="wide")

st.title("🛡️ Seguridad y Cumplimiento Normativo")
st.markdown("Monitorización de amenazas perimetrales y estado de certificaciones.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Estado de Auditoría y Cumplimiento")
    st.progress(85, text="Progreso para recertificación ISO 27001 (85%)")
    
    st.write("")
    st.success("✅ **Control de Acceso Biométrico:** Activo en todos los racks.")
    st.success("✅ **Encriptación de Datos:** AES-256 para datos en reposo.")
    st.warning("⚠️ **Simulacro de Recuperación (DRP):** Pendiente (15 de Mayo).")
    st.error("🚨 **Actualización de Firmware:** 2 switches pendientes.")

with col2:
    st.subheader("Amenazas Mitigadas (Últimos 7 días)")
    st.write("Intentos de intrusión bloqueados por el Firewall de AWS:")
    
    # Datos simulados de ciberseguridad
    threats = pd.DataFrame({
        "Día": ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
        "Ataques DDoS": [120, 150, 80, 220, 105, 50, 75],
        "Intentos Malware": [40, 25, 55, 10, 30, 5, 15]
    }).set_index("Día")
    
    # Colores personalizados para la gráfica
    st.bar_chart(threats, color=["#FF4B4B", "#FFA500"])