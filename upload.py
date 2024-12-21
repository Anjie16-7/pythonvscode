import streamlit as st
import pandas as pd
import plotly.express as px

menu = st.sidebar.selectbox("Choose an option", ['Upload CSV','Upload Image','Upload Audio','Upload Video'])

if menu == 'Upload CSV' :
    st.subheader("Upload CSV & View Database")
    uploadcsv = st.file_uploader("Upload your CSV file here", type='csv')
    if uploadcsv:
        readcsv = pd.read_csv(uploadcsv)
        with st.expander("View Table:"):
            st.table(readcsv)
        read= readcsv.columns#read columns
        select=st.multiselect("Choose column to plot:",read)
        c1,c2=st.columns(2)
        with c1:
            operate=st.radio("Choose Operator",["Average","Sum","Count"])
        with c2:
            chart=st.radio("Choose Type Of Chart",["Pie Chart","Bar Chart"])

        if select:
            if operate=="Average":
                values=readcsv[select].mean().reset_index()
                st.table(values)
                if chart=="Bar Chart":
                    bar= px.bar(values,x= 'index', y=0,labels={'index':'Subject','0':'Average'})
                    st.plotly_chart(bar)
                elif operate== 'Pie Chart':
                    pie = px.pie(values, names= 'index', values=0, labels={'index':'Subject','0':'Average'})
                    st.plotly_chart(pie)





if menu== "Upload Image":
    st.subheader("Upload Image")
    uploadimage= st.file_uploader("Upload Image:",type=["png","jpeg","webp","jpg"])
    if uploadimage:
        with st.expander("View Image"):
            st.image(uploadimage)

if menu == 'Upload Audio':
    st.subheader ("Upload Audio")
    uploadaudio = st.file_uploader('Upload your audio file here', type=['mp3','wav' ])
    if uploadaudio:
        st.audio(uploadaudio, format='audio/mp3')

if menu == 'Upload Video':
    st.subheader('Upload Video Link')
    link= st.text_input("Paste Link:")
    try:
        if link:   
            if st.button("Show"):
                    video= st.video(link)

    except:
        st.error("Link inputed isn't working")

#ability test on uploadCSV
# use a multiselect to choose columns to plot: create a variable called columnslist = 'read your pandas file'.to_list()
# use a radio to choose statistical operators (sum,average,count) #check your previous work