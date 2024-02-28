# Savings App
# Create a python program to ask how much a user wants to save on Monday, Tuesday, up to sunday  
# Add up all his savings
# Show him the total savings for the week

import streamlit as st

st.title("Welcome To Managing Your Savings")
Mon=st.number_input("What do you want to save on Monday: ")
Tue=st.number_input("What do you want to save on Tuesday: ")
Wed=st.number_input("What do you want to save on Wednesday:")
Thur=st.number_input("What do you want to save on Thursday: ")
Fri=st.number_input("What do you want to save on Friday: ")
Sat= st.number_input("What do you want t save on Saturday: ")
Sun=st.number_input("What do you want to save on Sunday: ")
total= Mon+Tue+Wed+Thur+Fri+Sat+Sun
see=st.button("Total Savings")
if see:
    st.write("You will have $",total,"at the end of the week")



    