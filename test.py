import pandas as pd
import streamlit as st
phone={"Phone type":[15,16,8],"Year":[2015,2007,2020],"Price":["$1650","$2000","$3600"]}
st.write(phone)
dict=pd.DataFrame(phone)
st.table(dict)