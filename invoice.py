import streamlit as st
from fpdf import FPDF
import base64 # convert python binary to printable characters
col1,col2,col3=st.columns(3)
with col2:
    st.title("Invoice")
with col1:
    logo = st.image("logo.png",120,120)

col4,col5=st.columns(2)
with col4:
    name=st.text_input("Bill to:",placeholder='Customer Name', )
    address= st.text_input('E',placeholder="Email Address",label_visibility= 'collapsed')
with col5:
    num=st.text_input('Invoice#:')
    date= st.date_input('Invoice Date:')
    due= st.date_input("Due Date:")


col6,col7,col8,col9=st.columns(4)
with col6:
    decript= st.text_input('Description', placeholder='Enter Description')
with col7:
     
    quantity=st.number_input("Quantity",0,100)
     
    
with col8:
    Price= st.number_input("Price per Unit")
with col9:    
    Total= quantity*Price
    show= st.text_input("Total Price",Total)
st.divider()
col10, col11=st.columns(2)
with col10:
    st.subheader("Payment info")
    sname= st.write("Acc Name:",name)
    snum= st.write("Acc Number:",num)
    st.write("Bank Name: UAE Bank",)
with col11:
    st.write("Payment Due")
    st.header(Total)
    

#function to generate our PDF


def generate_pdf():
     pdf = FPDF()


     #Add a page
     pdf.add_page()


     #Set your default fonts
     pdf.set_font("Arial", size=12)


     #Set column1 x and y coord
     col1x = 10
     col1y = 100


     #Add image
     pdf.image("Logo.png",x=col1x, y=col1y)






     
     #Save the PDF
     pdf_file = 'invoice.pdf'
     pdf.output(pdf_file)
     return pdf_file


#Generate the PDF
pdf_func = generate_pdf()


#Read the PDF FUNCT as binary data
with open(pdf_func, 'rb') as binary:
     pdf_data = binary.read()


if st.button(":blue[View Invoice]"):
     #Write the PDF using base64
     pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')


     #Generate the HTML to embed the PDF
     pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="100%" height="600px" />'


     #Display the embedded pdf (Markdown helps us use HTML in streamlit)
     st.markdown(pdf_embed,unsafe_allow_html=True)




