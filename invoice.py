import streamlit as st
col1,col2,col3=st.columns(3)
with col2:
    st.title("Invoice")
with col1:
    logo = st.image("logo.png",120,120)

