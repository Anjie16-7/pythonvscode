import streamlit as st 
import pandas as pd
menu=st.sidebar.selectbox("Menu",["Register Student","Add Payment","Admin Settings"])

join= pd.read_csv("schoolfees.csv")
with st.form("Register Student",clear_on_submit=True):
    if menu=="Register Student":
        st.subheader(f":blue[Register]")
        st.divider()
        c1,c2=st.columns(2)
        with c1:
            cname=st.text_input("Student's First and Last Name:")
        with c2:
            year= st.selectbox("Select Year",["Year 1","Year 2","Year 3","Year 4","Year 5","Year 6","Year 7","Year 8","Year 9","Year 10","Year 11","Year 12"])
        st.divider()
        st.subheader(f':blue[Parent Info]')
        st.divider()
        c3,c4=st.columns(2)
        with c3:
            pname=st.text_input("Parent's First and Last Name:")
        with c4:
            email=st.text_input("Enter Parent's Email:")
        st.divider()
        st.subheader(f":blue[Contact Info]")
        st.divider()
        c5,c6=st.columns(2)
        with c5:
            num=st.text_input("Enter Parent's Number:")
        with c6:
            address=st.text_input("Enter Home Address:")
       
       
        if st.form_submit_button("Register Student"):
            st. write("Student has been registered")
            diction={"Student Name":cname,"Year":year,"Parent Name":pname,"Email":email,"Number":num,"Address":address}
            table=pd.DataFrame(diction)
            tab2=