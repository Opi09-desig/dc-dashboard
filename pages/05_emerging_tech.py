import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AWS QRO-1 | Emerging Tech", layout="wide")

# --- CSS PARA IDENTIDAD VISUAL (AWS PURPLE/GOLD) ---
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




st.title("🔭 Emerging Technologies Radar")
st.subheader("Strategic Roadmap 2024 - 2030 | AWS Mexico Central")

# --- RADAR TECNOLÓGICO (REQUISITO GUÍA) ---
st.write("Assessment of technology maturity and impact for the next decade.")

# Datos para el Radar
categories = ['Impact', 'Feasibility', 'ROI', 'Security', 'Sustainability']
fig_radar = go.Figure()

fig_radar.add_trace(go.Scatterpolar(
      r=[5, 4, 5, 3, 5],
      theta=categories,
      fill='toself',
      name='Liquid Cooling (GenAI Ready)',
      line_color='#c9a84c'
))
fig_radar.add_trace(go.Scatterpolar(
      r=[4, 5, 4, 5, 3],
      theta=categories,
      fill='toself',
      name='AI Ops (Predictive)',
      line_color='#7b2fb5'
))

fig_radar.update_layout(
  polar=dict(
    radialaxis=dict(visible=True, range=[0, 5], gridcolor="#30363d"),
    bgcolor="#161b22"
  ),
  showlegend=True,
  template="plotly_dark",
  paper_bgcolor='rgba(0,0,0,0)'
)

st.plotly_chart(fig_radar, use_container_width=True)

# --- TIMELINE DE ADOPCIÓN (REQUISITO GUÍA) ---
st.divider()
st.subheader("📅 Adoption Timeline 2024 - 2030")

timeline_data = pd.DataFrame([
    dict(Task="Edge Computing Expansion", Start='2024-01-01', Finish='2026-12-31', Resource="Market Entry"),
    dict(Task="Liquid Cooling Migration", Start='2025-06-01', Finish='2027-12-31', Resource="Infrastructure"),
    dict(Task="Hydrogen Fuel Cells Pilot", Start='2027-01-01', Finish='2029-12-31', Resource="Sustainability"),
    dict(Task="Quantum Networking Nodes", Start='2029-01-01', Finish='2030-12-31', Resource="Advanced R&D")
])

fig_timeline = px.timeline(timeline_data, x_start="Start", x_end="Finish", y="Task", color="Resource",
                           template="plotly_dark", color_discrete_sequence=["#7b2fb5", "#c9a84c", "#00C853", "#FF4B4B"])
fig_timeline.update_yaxes(autorange="reversed")
st.plotly_chart(fig_timeline, use_container_width=True)

# --- RECOMENDACIONES ESTRATÉGICAS ---
st.subheader("💡 Strategic Recommendations")
col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Short Term (2024-2026):**
    Accelerate **Liquid Cooling** adoption. Querétaro's climate requires efficient thermal management as server density increases for AI workloads.
    """)

with col2:
    st.success("""
    **Long Term (2027-2030):**
    Integrate **Hydrogen Fuel Cells**. To reach net-zero goals in Mexico, we must move beyond traditional diesel generators for backup power.
    """)