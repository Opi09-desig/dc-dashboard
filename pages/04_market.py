import streamlit as st
import plotly.express as px

st.title("📈 04 · Market Intelligence (U4)")
st.write("### Mexico Data Center Market & Regional Hotspots")

# Datos de tu investigación
market_data = {
    'Region': ['Querétaro', 'Edo. México', 'Monterrey', 'Others'],
    'Capacity (MW)': [60, 25, 10, 5]
}

fig = px.bar(market_data, x='Region', y='Capacity (MW)', title="DC Capacity by Region in Mexico")
st.plotly_chart(fig)

st.warning("Dato Clave: Inversión proyectada de AWS en Querétaro: $5 Billion USD.")