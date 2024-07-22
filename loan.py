import streamlit as st
side=st.sidebar.selectbox("Menu",['Input Data',"..."])
if side=='Input Data':
    c1,c2,c3=st.columns(3)
    with c2:
        st.title("Loan")
    st.header(f":blue[Personal Info]")
    c4,c5=st.columns(2)
    
    with c4:
        name=st.text_input('Enter Name Here:')
        age= st.number_input("Enter Age Here:",0,150)
    with c5:
        address=st.text_input('Enter Address Here:')
        email=st.text_input('Enter Email Here:')
    c6,c7,c8=st.columns(3)
    with c7:
        bankname=st.text_input("Enter Bank's Name Here")
    st.divider()
   
   # how much
    #when collected
    #interesrt
  #  money owed
   # if st.button("Done") and age<18:
   #     st.write("Your are not eligible to collect loans")
    
