#Create a Simple python application that recognizes Odd numbers and Even numbers.
 #Accept user input
 #Print to the screen what number  user entered.
import streamlit as st

st.title("Even or Odd?")
name=st.text_input("Input Name Here:")
num=st.number_input("Write Number Here",0,900)
test= num%2
if st.button("Done") and test==0:
    st.write(name,",the number you have entered is even")
else:
    st.write(name,",the number you have entered is odd")


