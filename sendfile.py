import streamlit as st
from email.message import EmailMessage #email configuration (sender, receiver, content)
import ssl #keep emails secured, only the receiver gets it
import smtplib #the email transfer

sender = 'aishafazyakinola9@gmail.com'
password = 'ughz xjmm vfbz nndi'

col1,col2 = st.columns(2)

with col1:
    receiver = st.text_input("Enter email to send to")

with col2:
    subject = st.text_input ('Enter email subject here')

body = st.text_area("Enter email message here",height=200)
uploadfile = st.file_uploader('Upload image or text files to attach to mail', type=['jpg', 'pdf','png','txt','csv','txt'])
try:
    email = EmailMessage()
    email['From'] = sender
    email['To' ] = receiver
    email['Subject'] = subject

    if uploadfile and receiver and body:

        if st.button("Send Mail"):

            filedata = uploadfile.read()
            filename = uploadfile.name

            email.add_attachment(filedata,maintype='application', subtype='octet stream', filename=filename)
    #octet stream: since youre not sure what type of data the user will upload. octet stream indicates any binary data

            context = ssl.create_default_context() 

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(sender,password)
                smtp.sendmail(sender,receiver,email.as_string())
                st.success("Email with Attachment Sent!")
    else:
        st.error("One or more of the boxes haven't been filled")
except:
    st.error("Something went wrong. Try Again.")