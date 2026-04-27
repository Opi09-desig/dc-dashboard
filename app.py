import streamlit as st

st.set_page_config(page_title="AWS QRO-1 | Command Center", layout="wide", page_icon="🌐")

# --- ESTILO CSS PARA UN LOOK PROFESIONAL ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #c9a84c; padding: 15px; border-radius: 10px; }
    .stAlert { background-color: #161b22; border: 1px solid #c9a84c; color: white; }
    .aws-banner {
        background: linear-gradient(135deg, #232f3e 0%, #1a1a1a 100%);
        padding: 40px;
        border-radius: 15px;
        border-left: 10px solid #c9a84c;
        color: white;
        text-align: left;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- BANNER PRINCIPAL ---
st.markdown("""
<div class="aws-banner">
    <h1 style="margin:0; color: #f5f5f0;">🌐 AWS Mexico Central (mx-central-1)</h1>
    <p style="margin:0; font-size: 20px; color: #c9a84c; font-weight: bold;">Data Center Operations & Strategic Command Center</p>
    <p style="margin-top:10px; font-size: 14px; opacity: 0.8;">Hyperscale Infrastructure Management • Querétaro, MX</p>
</div>
""", unsafe_allow_html=True)

# --- MÉTRICAS DE NIVEL REGIONAL ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Operational SLA", "99.999%", "Target Achieved")
with col2:
    st.metric("Total Regional Investment", "$5.0B USD", "Approved 2024")
with col3:
    st.metric("Current PUE (Avg)", "1.18", "-0.02 Efficiency", delta_color="normal")

st.divider()

# --- CUERPO PRINCIPAL ---
col_text, col_tech = st.columns([1.5, 1])

with col_text:
    st.subheader("Executive Summary")
    st.write("""
    Esta plataforma gestiona la estrategia operativa de la nueva región de AWS en México. 
    Nuestro enfoque integra los tres pilares de la Ingeniería de Datos moderna:
    
    * **Resilience (U3):** Arquitectura Serverless sobre AWS ECS Fargate para eliminar puntos únicos de falla físicos.
    * **Sustainability (U3):** Monitoreo en tiempo real de eficiencia energética alineado con los objetivos de 'Net-Zero'.
    * **Market Intelligence (U4):** Análisis financiero del impacto de caídas y ventaja competitiva frente a otros proveedores en la región del Bajío.
    """)
    
    st.success(" **Project Goal:** Optimizar la gestión de infraestructura crítica mediante la orquestación de contenedores y automatización en la nube.")

with col_tech:
    st.markdown("""
    <div style="background-color: #161b22; padding: 20px; border-radius: 10px; border: 1px solid #30363d;">
        <h4 style="color: #c9a84c; margin-top:0;">🛠️ Enterprise Stack</h4>
        <ul style="list-style-type: none; padding-left: 0;">
            <li>🔹 <b>Frontend:</b> Streamlit (Python 3.11)</li>
            <li>🔹 <b>Orchestration:</b> AWS ECS Fargate</li>
            <li>🔹 <b>Registry:</b> AWS ECR</li>
            <li>🔹 <b>IaC:</b> Terraform Cloud</li>
            <li>🔹 <b>CI/CD:</b> GitHub Actions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.info(f"📍 **Location:** Querétaro Hub\n\n📅 **Status:** Production Ready")