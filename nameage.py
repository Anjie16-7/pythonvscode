import streamlit as st
import pandas as pd
csvlink= pd.read_csv('namage.csv')
selectmenu = st.sidebar.selectbox('Select menu', ['Enter Data', 'Database'])
if selectmenu=='Enter Data':
    name= st.text_input('Enter Student Name:')
    age=st.number_input('Enter Student Age',3,22)
    if st.button('Submit Data'):
        dict={'Name':[name],"Age":[age]}
        tab=pd.DataFrame(dict)
     #   st.table(tab)
        tab2=pd.concat([csvlink,tab],ignore_index=True)
        tab2.to_csv("namage.csv",index=False)
   
if selectmenu=='Database':
    st.table(csvlink)
   
