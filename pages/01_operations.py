import streamlit as st

st.title("📊 01 · Data Center Operations (U3)")
st.subheader("Uptime SLA & Incident Management")

col1, col2 = st.columns(2)
col1.metric("Current SLA", "99.999%", "Available")
col2.metric("Active Incidents", "0", "Stable")

st.write("### MAC Processes (Moves, Adds, Changes)")
st.table({"ID": ["MAC-001", "MAC-002"], "Type": ["Server Install", "Cable Cleanup"], "Status": ["Pending", "In Progress"]})