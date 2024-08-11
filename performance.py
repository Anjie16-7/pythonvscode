import streamlit as st
import pandas as pd
import plotly.express as px
cl=pd.read_csv("perform.csv")

menu=st.sidebar.selectbox("Menu",['Input Data',"Database","Charts"])
if menu=="Input Data":
    t1,t2,t3=st.columns([1,2,1])
    with t2:
        st.title(f':blue[Football Season]')
    s1,s2=st.columns(2)
    with s1:
        name=st.text_input("Player's Name:")
        weight=st.text_input("Player's weight (kg):",0,100)
        
    with s2:
        age=st.text_input("Player's Age:")
        games=st.text_input("No. of games played:")

    d1,d2,d3=st.columns(3)
    with d1:
        tackles=st.text_input("Number of tackles:" )
    with d2:
        goals=st.text_input("Number of goals scored:")
    with d3:
        assists=st.text_input("Number of assists:")
    but=st.button("Done")
    if but:
        sc1,sc2,sc3=st.columns(3)
        with sc1:
            st.success("Data has been saved")
        dict={"Name":[name],"Weight":[weight],"Age":[age],"Games":[games],"Tackles":[tackles],"Goals":[goals],"Assists":[assists]}
        table = pd.DataFrame(dict)
        table2= pd.concat([cl,table],ignore_index=True)
        table2.to_csv('perform.csv',index=False)
if menu=="Database":
    st.title(":blue[Database]")
    st.table(cl)

if menu=="Charts":
    f1,f2,f3=st.columns([1,2,1])
    with f2:
        st.title(f':blue[Charts]')
    values= ["Games","Tackles","Goals","Assists"]
    
    cn1,cn2,cn3=st.columns(3)
    with cn2:
        chose=st.selectbox("Which Chart:",["Bar Chart","Pie Chart"])
    if chose=='Pie Chart':
        valuestab = cl[values].mean().reset_index()
        #st.table(valuestab)
        rcolumns=valuestab.rename(columns={"index":"Performance",0:"Average"})
        piechart=px.pie(rcolumns,names='Performance',values="Average")
        st.plotly_chart(piechart)
    

    if chose=='Bar Chart':
        valuestable = cl[values].value_counts().reset_index()
        #st.table(cl)
        stat1,stat2,stat3=st.columns([1,3,1])
        with stat2:
            select=st.radio("Which Stats Do You Wish To View:",["Games","Tackles","Goals","Assists"],horizontal=True)
        if select == "Games":
            barchart = px.bar(cl,x='Name',y='Games')
            st.plotly_chart(barchart)
        if select == "Tackles":
            barchart = px.bar(cl,x='Name',y='Tackles')
            st.plotly_chart(barchart)
        if select == "Goals":
            barchart = px.bar(cl,x='Name',y='Goals')
            st.plotly_chart(barchart)
        if select == "Assists":
            barchart = px.bar(cl,x='Name',y='Assists')
            st.plotly_chart(barchart)
        
    
  
    
   
    
    