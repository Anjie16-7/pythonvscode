#Create a python program using Streamlit that accepts user age for a voting exercise.
#Minimum age for voting 18 years.
#When user enters an age number less than the minimum age, the response they get should be “You are not eligible to vote” otherwise they get “Congratulations! You are eligible to vote”.
import streamlit as st
st.title(':blue[Age to Vote]')
pic=st.image("logo.png",125,125)
st.write("Welcome to our website where you can check if you can officially vote!")

age= st.number_input("Enter age here:",1)

if st.button("Done"):
    if age<18:
        st.write('You are eligible to vote come again later')
    else:
        st.write("Congratulations! You are eligible to vote.")