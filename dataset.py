import streamlit as st
import pandas as pd
import plotly.express as px

link=pd.read_csv("bayern.csv")

result=["Win Loss"]
tab=link[result].value_counts().reset_index()
st.table(tab)
renamedcolumns = tab.rename(columns={'Win Loss': 'Results',"count":'Total'})
barchart = px.bar(renamedcolumns,x="Results",y='Total')
st.plotly_chart(barchart)