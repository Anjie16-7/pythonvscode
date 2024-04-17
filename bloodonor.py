
# Create a menu for Registration and Database
# Design a blood donation application that can get donor input
# -Name -Contact Number (use text)
# -Blood group (selectbox) -
#Disease/Infection (use radio )
# 'A', 'B', 'AB', 'O'
# -Submit donor details
# Next, save these in a csv file and show the database in a Database page in the menu
import streamlit as st
import pandas as pd
csv=pd.read_csv('donor.csv')
menu=st.sidebar.selectbox("Menu",['Registration','Database'])
if menu=='Registration':
    st.title(':orange[Register Here]')
    
    name=st.text_input("Your Name:")
    age=st.number_input('Age:',18,60)
    col3,col4=st.columns(2)
    with col3:
        gender=st.radio('Gender',['Male','Female'],horizontal=True)
    with col4:
        disease= st.radio("Any Diseases or Infections?",['Yes','No'],horizontal=True)
    group= st.selectbox('Blood Group',['A','B','AB','O'])
    num=st.text_input("Contact Number:")
    if st.button('Submit'):
        col1,col2=st.columns(2)
        with col1:
            st.success('Your infomation has been entered')
        data={'Name':[name],'Age':[age],'Gender':[gender],'Disease':[disease],'Blood Group':[group],'Contact Number':[num]}
        table=pd.DataFrame(data)
        table2=pd.concat([csv,table],ignore_index=True)
        table2.to_csv('donor.csv',index=False)

if menu=='Database':
    st.title(':orange[Database]')
    st.table(csv)
    
        
    
    