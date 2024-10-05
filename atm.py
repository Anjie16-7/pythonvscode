import streamlit as st
#Create an ATM machine using python streamlit.

#Check balance
#Withdraw
#Deposit

#Make use of button, success notifications and error validation.



menu=st.sidebar.selectbox("Menu",["Check Balance","Withdraw and Deposit"])
balance=15000
if menu=="Check Balance":
    t1,t2,t3=st.columns([1,3,1])
    with t2:
        st.title(f":blue[Bank Account]")
    st.success(balance)

if menu=="Withdraw and Deposit":
    c1,c2=st.columns(2)
    with c1:
        minus=st.number_input("Enter Withdraw Amount($)")
    
    if st.button("Done"):
        if minus>balance:
            st.error("Do not have enough money in the bank")
        else:
            st.write("Money has been withdrawed")
            total=balance-minus
        
        st.success(total)

if menu=="Deposit":
    add=st.number_input("Enter Deposit Amount($)")
    if st.button("Finished"):
        st.success("Money has been deposited")
        total=balance+add
        st.success(total)



