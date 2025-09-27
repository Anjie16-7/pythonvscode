import streamlit as st 

n = {'a':'yes','no':2,'c':'yes'}

for key,value in n.items():
    if value == 'yes':
       st.write('Question',key,'has not been answered yet')
