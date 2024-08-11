import streamlit as st 
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')


csvlink= pd.read_csv('score.csv')


selectmenu = st.sidebar.selectbox('Select menu', ['Scores', 'Database'])
if selectmenu=='Scores':
    st.title("Student Scores")
    name= st.text_input('What is your name:')


    col1, col2=st.columns(2)
    with col1:
        maths=st.number_input ('Score for maths: ',0,100)
        eng=st.number_input('Score for english: ',0,100)
        bio=st.number_input('Score for biology: ',0,100)

    with col2:
        fre=st.number_input('Score for french: ',0,100)
        chem=st.number_input('Score for chemistry: ',0,100)

    total= maths+eng+bio+fre+chem
    av= round(total/5,2)
    ave=str(av)
    if av>70:
        grade= 'A'
    elif av>60:
        grade= 'B'
    elif av>50:
        grade= 'C'
    elif av>45:
        grade= 'D'
    elif av>40:
        grade= 'E'
    else:
        grade= 'F'
    if st.button('Show results'):
        sn1,sn2,sn3=st.columns(3)
        with sn1:
            st.success("Students scores submitted to Database")
        dict={"Name":[name],"Maths":[maths],"English":[eng],"Biology":[bio],"French":[fre],"Chemistry":[chem],"Total":[total],"Average":[ave]}
        table=pd.DataFrame(dict)
        #st.table(table)
        table2= pd.concat([csvlink,table],ignore_index=True)#merges the data shown for intial input and puts in csv table and saves it
        table2.to_csv("score.csv",index=False)#to ignore the idex positions

if selectmenu=="Database":
    st.title("Student Database")
    st.table(csvlink)
    subjects = ['Maths', 'English', 'Biology', 'French', 'Chemistry']
    
    subjectstable = csvlink[subjects].mean().reset_index()
    renamedcolumns = subjectstable.rename(columns={'index': 'Subject',0:'Average'})
    # st.table(renamedcolumns)
    
    barchart = px.bar(renamedcolumns,x='Subject',y='Average')
    piechart = px.pie(renamedcolumns, names='Subject', values='Average')
    s1,s2,s3=st.columns(3)
    with s1:
        chosebc=st.selectbox("Charts",['barchart','piechart'])
    if chosebc=='barchart':
        
           
        
        st.plotly_chart(barchart)
    if chosebc=='piechart':
        st.plotly_chart(piechart)
