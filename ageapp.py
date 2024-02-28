import streamlit as st

st.title("Welcome to my age calculator")
name= st.text_input("Enter your name: ")
cy= st.number_input("Enter current year: ",2023)
yob= st.number_input("Enter your year of birth: ",1950,2023)
age= cy-yob
show= st.button("Check age")
if show:
    st.write(name,"you will be",age,"in",cy)


