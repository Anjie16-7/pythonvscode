import streamlit as st
import pandas as pd
st.set_page_config(page_title='Loans', page_icon="📕",layout="centered", initial_sidebar_state="expanded")
link=pd.read_csv("loan.csv")
side=st.sidebar.selectbox("Menu",['Input Data',"Database"])
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
        bn=st.text_input("Enter Bank's Name Here")
    st.divider()
    e1,e2,e3,e4=st.columns(4)
    with e1:
        amount=st.number_input("Amount of Money Borrowed")
    with e2:
        date=st.date_input("Date Loan Was Collected")
        year=date.year
        import datetime
        now= datetime.datetime.now()
        now2=now.year
        time=now2-year
        st.write("Number of Years:",time)
    with e3:
        interest=st.number_input('Interest per annum(%)')
        
        owed=(amount*(interest/100))*time
        
        st.write("Interest owed:",f'${owed:,}')
    with e4:
        total=amount+owed
        st.text_input("Total Owed",f'${total:,}')
    
    if st.button("Done"):
      if age<18:
        st.error("You are not eligible to collect loans as you are below 18")
      else:
        w1,w2,w3=st.columns(3)
        with w1:
              st.success('Your Data has being stored')
              dict={'Name':[name],"Age":[age],"Address":[address],"Email":[email],"Bank Name":[bn],"Amount Borrowed":[amount],"Date Borrowed":[date],"Interest(%)":[interest],"Interest Owed":[owed],"Total Owed":[total]}
              tab=pd.DataFrame(dict)
              table2= pd.concat([link,tab],ignore_index=True)
              table2.to_csv("loan.csv",index=False)
if side=='Database':
    st.title(":blue[Database]")
    st.table(link)
    
