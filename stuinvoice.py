import streamlit as st 
import pandas as pd
st.set_page_config(page_title="Student Invoice",page_icon="📕")
menu=st.sidebar.selectbox("Menu",["Register Student","School Fees","Download Reiceipt","Admin Settings"])


csvlink=pd.read_csv('stu.csv')
studentID="StudentID"+str(len(csvlink)+1)

with st.form("Register Student", clear_on_submit=True):
        if menu=="Register Student":
            st.title(f":blue[Register]")
            col1,col2=st.columns(2)
            with col1:
                name= st.text_input("Child's Full Name:")
            with col2:
                year= st.number_input("What class is your child in:",1,12)
                year="Year"+str(year)
                
            st.divider()   
            
            st.subheader("Parent Info")
            pl1,pl2=st.columns(2)
            with pl1:
                pname=st.text_input("Enter Your Name:")
                email=st.text_input("Enter Email:",placeholder="@gmail.com")
            with pl2:
                phone=st.text_input("Enter Your Number:")
                address=st.text_input("Enter Your Address")
                
            if st.form_submit_button("Done"):
                st.write("Your Child Has Been Registered")

            dict= {"StudentID":[studentID],"Child Name":[name],"Year":[year],"Parent Name":[pname],"Email":[email],'Phone Number':[phone],"Address":[address]}
            tab= pd.DataFrame(dict)
            table2= pd.concat([csvlink,tab],ignore_index=False)
            table2.to_csv("stu.csv",index=False)        
    
if menu == 'School Fees':

    c,co,col = st.columns(3)

    with col:

        search = st.text_input("Enter student ID")
        savebutton = st.button("Search Student's ID")

    if savebutton:
        if search:
            searchresult = csvlink[csvlink['StudentID' ].str.lower()== search.lower()]
            st.table(searchresult)
            gname=searchresult["Child Name"].iloc[0]
            gyear=searchresult["Year"].iloc[0]
            st.title(f':blue[{gname}]')
            st.subheader(gyear)
if menu=="Admin Settings":

    login=st.sidebar.text_input("Enter Password:",type="password")
    if login=="2468":
        st.success("Correct")