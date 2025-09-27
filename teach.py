

import streamlit as st  
# Ire

st.title("Skickers")
name= st.text_input("Enter your name:")

animal_stickers=st.number_input("How many animal stickers do you have?",0)
superhero_stickers= st.number_input("How many superhero stickers do you have?",0)
star_stickers= st.number_input("How many star stickers do you have?",0)

total= animal_stickers+superhero_stickers+star_stickers




if st.button("Done"):
    st.write("Hi,",name,". You have",total,"number of stickers!")

    

