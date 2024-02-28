#create a simple page for a school. Show on the page the Elementary fee is 5000 dollars and the college fee is 15000 dollars
#Ask how many kids the parent have for elementary and ask if they have for college
#create a dictionary and convert all information to a dataframe after clicking a submit button


import streamlit as st
import pandas as pd
st.title("Welcome")
st.subheader("Elementary fee: $5000")
st.subheader("College fee: $15000")
nums=st.number_input("How many of your children go to elementary school?",0,100)
numc=st.number_input("How many of your children go to college?",0,100)
efee=5000*nums
cfee=15000*numc
total=efee+cfee
if st.button("Show Results"):
    st.write("Elementary fees:",efee,"College fees:",cfee,"Total fees:",total)
    dic={"Number of kids for elementary":[nums],"Number of kids for college":[numc],"Elementary fees":[efee],"College":[cfee],"Total fees":[total]}
    table= pd.DataFrame(dic)
    st.table(table)
