import streamlit as st
import fpdf as FPDF

t1,t2,t3=st.columns([1,9,1])
with t2:
    st.title(f":blue[Doctor Appointment Form]")
st.divider()
d1,d2=st.columns(2)
with d1:
    st.text_input("Name",placeholder='First Name')
with d2:
    st.text_input(" ",placeholder='Last Name')
    
b1,b2,b3=st.columns(3)
with b1:
    day=st.text_input("Date Of Birth",placeholder='Enter Day')
with b2:
    month=st.selectbox(" ",['January','February','March','April','May','June','July','August','September','Ocotber','November','December'])
with b3:
    year=st.text_input("",placeholder='Enter Year')
r1,r2=st.columns(2)
with r1:
    gen=st.selectbox("Gender",['Male','Female'])
    address=st.text_input("Enter Address")
    state=st.text_input("State/Province")
with r2:
    num=st.text_input("Phone Number",placeholder='(000)000-0000')
    city=st.text_input("City")
    zip=st.text_input("Zip Code")
email=st.text_input("Email",placeholder="ex: myname@example.com")
facility=st.radio('Have you ever applied to our facility before',["Yes","No"])

def generate_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
