import streamlit as st
#to make a python program run on the webpage
from email.message import EmailMessage
#to setup email config: sender, receiver, content
import ssl
#keep email safe on the internet so that noone except the receiver can get it
import smtplib
#this is in charge of sending the message from the sender to the receiver (simple message transfer protocol)

sender = 'aishafazyakinola9@gmail.com'
password ='ughz xjmm vfbz nndi'

receiver = st.text_input("Enter the email to send to")
subject = st.text_input("Enter the email subject here")
body = st.text_area("Enter the email content here",height=200)

if st.button("Send Email"):
    email = EmailMessage() #we want to create a new email message
    email['From' ] = sender
    email['To' ] = receiver
    email['subject'] = subject
    email.set_content(body) #this is the body/content of the email

    securecontents = ssl.create_default_context()
    #this creates a secure connection, no one else apart from the receiver can get this

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=securecontents) as smtp: #hostname, port, ssl
    #this help us to connet with the gmail server
        smtp.login(sender,password) #this login to sender email address and password
        smtp.sendmail(sender,receiver, email.as_string()) #sends email to the receiver as a string so he can easily read
        st.success ('Thank you. Message sent')