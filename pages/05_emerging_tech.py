import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="AWS QRO-1 | Emerging Tech", layout="wide")

# --- CSS PARA IDENTIDAD VISUAL (AWS PURPLE/GOLD) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border: 1px solid #7b2fb5; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

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