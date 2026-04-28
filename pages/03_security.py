import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AWS QRO-1 | Security & Compliance", layout="wide")

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

st.title("🛡️ Security & Compliance Center")
st.subheader("AWS Mexico Central | Region Security Operations")

# --- INDICADORES DE RIESGO ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Threat Level", "Low", "Stable", delta_color="normal")
with col2:
    st.metric("Compliance Score", "94%", "+2%")
with col3:
    st.metric("Blocked Attacks", "1,240", "+15%")
with col4:
    st.metric("Physical Perimeter", "Secure", "Verified")

st.divider()

col_left, col_right = st.columns([1, 1])

with col_left:
    st.subheader("📋 Compliance Checklist (TIA-942 / ISO)")
    st.write("Current readiness for the QRO-1 Facility audit.")
    
    # Requisitos basados en la guía
    st.progress(94, text="ISO 27001 / TIA-942 Readiness")
    
    with st.container():
        st.write("### Critical Controls")
        st.success("✅ **Physical Access:** Biometric & Multi-factor authentication active.")
        st.success("✅ **Data Encryption:** AES-256 at rest and TLS 1.3 in transit.")
        st.warning("⚠️ **DRP Drill:** Disaster Recovery simulation scheduled for May 15.")
        st.info("ℹ️ **CCTV Audit:** Quarterly review in progress.")

with col_right:
    st.subheader("🛡️ AWS WAF & Shield Activity")
    st.write("Intrusion attempts mitigated in the last 7 days.")
    
    threats_data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "DDoS Mitigation": [120, 150, 80, 220, 105, 50, 75],
        "SQL Injections": [40, 25, 55, 10, 30, 5, 15]
    })
    
    fig_threats = px.bar(threats_data, x="Day", y=["DDoS Mitigation", "SQL Injections"],
                        barmode="group", template="plotly_dark",
                        color_discrete_sequence=["#ff4b4b", "#ffa500"])
    
    fig_threats.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_threats, use_container_width=True)

# --- SECCIÓN EXTRA: SHARED RESPONSIBILITY MODEL ---
st.subheader("🤝 Shared Responsibility Model")
st.image("https://d1.awsstatic.com/security-center/Shared_Responsibility_Model_V2.59d1ec054433410ccba8a650918b953874c4ee57.jpg", 
         caption="AWS is responsible for security OF the cloud, we are responsible for security IN the cloud.", width=600)