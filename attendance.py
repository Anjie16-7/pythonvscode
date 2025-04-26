import streamlit as st
import pandas as pd
import plotly.express as px

csvlink=pd.read_csv("attendance.csv")

menu= st.sidebar.selectbox("Menu",["Record","Data Table"])
st.sidebar.link_button("Question Link","https://stemhackathon.com/question-1-data-apps-hard/")
if menu=="Record":
    st.title("Attendance Tracker")
    col1,col2=st.columns(2)

    with col1:
        name= st.text_input("Enter Student's Name:")
        seat=st.text_input("Enter Seat Number:")
    with col2:
        here= st.text_input("Total Days Present:")
        away= st.text_input("Total Days Absent:")
    if st.button("Done"):
        st.success("Data has been stored")
        dict={"Name":[name],"Seat":[seat],"Present":[here],"Absent":[away]}
        
        table=pd.DataFrame(dict)
        tab2=pd.concat([csvlink,table],ignore_index=True)
        tab2.to_csv("attendance.csv",index=False)
        st.write(dict)
        st.table(tab2)

        
if menu=="Data Table":

    barchart= px.bar(csvlink,x="Name",y=["Absent","Present"],barmode="group")
    st.plotly_chart(barchart)





