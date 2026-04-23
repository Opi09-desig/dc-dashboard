import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Gestión de Operaciones")
st.write("Control de carga y rendimiento de servidores.")

# Gráfico simulado de carga de trabajo
data = pd.DataFrame(np.random.randn(20, 3), columns=['Cómputo', 'Red', 'Storage'])
st.line_chart(data)

st.success("Estado de los sistemas: Operando normalmente")