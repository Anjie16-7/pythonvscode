import streamlit as st
from email.message import EmailMessage
import ssl #used for secure connection between sender and reciever email (username, password, info)
import smtplib #used to send emails (needed with the email.message lib) SIMPLE MAIL

sender = 'aishafazyakinola9@gmail.com'
password = 'ughz xjmm vfbz nndi'

receive = st.text_input("Enter email to send to")

subject = st.text_input("Enter Email Subject here")

body = st.text_area("Enter Email Content here",height=200)



if st.button("Send mail"):
    email = EmailMessage()
    email['From'] = sender
    email['To'] = receive
    email[ 'subject'] = subject
    email.set_content(body) #this will set the body variable as the content
    securecontents = ssl.create_default_context() #this ensures email content is secures (hostname, port, ssl)

    with smtplib.SMTP_SSL('smtp.gmail.com',465, context=securecontents) as smtp: #(hostname, port, ssl)
        smtp.login(sender,password)
        smtp.sendmail(sender,receive,email.as_string()) #send email as strings