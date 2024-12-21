import streamlit as st
import pandas as pd 

csv= pd.read_csv("donate.csv")

menu=st.sidebar.selectbox("Menu",["Create Donation",'View Donation'])
with st.form("Create Donation",clear_on_submit=True):
    
    if menu=="Create Donation":

        st.title(f":blue[Create Donation]")
        st.divider()
        c1,c2=st.columns(2)
        with c1:
            title=st.text_input("Campaign Title:")
        with c2:
            email=st.text_input("Email:")
        st.divider()
        content=st.text_area("Campaign Details:")
        goal=st.number_input("Goal Amount")
        if st.form_submit_button("Create"):
            s1,s2=st.columns(2)
            with s1:
                st.success("Donation has been created!")

        dict={"Title":[title],"Email":[email],"Details":[content],"Goal":[goal]}
        table=pd.DataFrame(dict)
        table2=pd.concat([table,csv],ignore_index=False)
        table2.to_csv("donate.csv",index=False)
if menu == 'View Donation':
    st.subheader(":blue[View Donation]")
    st.divider()
    alltitles = csv['Title'].to_list()
   
    col1, col2 = st.columns(2)
    with col1:
        selectitle = st.selectbox("Select Donation To View", alltitles)

    filter= csv[csv['Title'] == selectitle]
    