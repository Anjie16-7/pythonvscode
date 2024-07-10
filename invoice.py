import streamlit as st
from fpdf import FPDF
import base64 # convert python binary to printable characters 
col1,col2,col3=st.columns(3)
with col3:
    st.title("Invoice")
with col1:
    logo = st.image("logo.png",120,120)
st.write('Lily Corporation')
st.write('237 Avenue Street, Al Barsha')
st.write("Dubai,UAE")
col4,col5=st.columns(2)
with col4:
    name=st.text_input("Bill to:",placeholder='Customer Name', )
    address= st.text_input('E',placeholder="Email Address",label_visibility= 'collapsed')
with col5:
    num=st.text_input('Invoice#:', placeholder="Invoice Number")
    date= st.date_input('Invoice Date:')
    ndate=str(date)
    due= st.date_input("Due Date:")
    ndue= str(due)


col6,col7,col8,col9=st.columns(4)
with col6:
    descript= st.text_input('Description', placeholder='Enter Description')
with col7:
     
    quantity=st.number_input("Quantity",0,100)
    nquantity=str(quantity)
     
    
with col8:
    Price= st.number_input("Price per Unit")
    nPrice=str(Price)
with col9:    
    Total= quantity*Price
    show= st.text_input("Total Price",Total)
    nTotal=str(Total)
st.divider()
col10, col11=st.columns(2)
with col10:
    st.subheader("Payment info")
    sname= st.write("Acc Name:",name)
    snum= st.write("Acc Number:",num)
    st.write("Bank Name: UAE Bank",)
with col11:
    st.write("Payment Due")
    st.header(f'${Total}')
    

#function to generate our PDF


def generate_pdf():
     pdf = FPDF()


     #Add a page
     pdf.add_page()


     #Set your default fonts
     pdf.set_font("Arial", size=12)


     #Set column1 x and y coord
     col1x = 10
     col1y = 15
     colw=45
     colh=10


     #Add image
     pdf.image("logo.png",x=col1x, y=col1y, w=45)
     pdf.set_font("Arial", size=21, style='B')

     pdf.set_xy(col1x+140,col1y+15)
     pdf.cell(colw,colh, txt='INVOICE',ln=True,align='L')

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+15,col1y+40)
     pdf.cell(colw,colh, txt='Lily Corporation:',ln=True, align='L' )

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+15,col1y+50)
     pdf.cell(colw,colh, txt='237 Avenue Street, Al Barsha',ln=True, align='L' )

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+15,col1y+60)
     pdf.cell(colw,colh, txt='Dubai UAE',ln=True, align='L' )

     pdf.set_font("Arial",size=15, style='B')
     pdf.set_xy(col1x+15,col1y+85)
     pdf.cell(colw,colh, txt='Bill to:',ln=True, align='L' )


     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+33,col1y+85)
     pdf.cell(colw,colh, txt=name,ln=True, align='L' )

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+15,col1y+95)
     pdf.cell(colw,colh, txt=address,ln=True, align='L' )

     pdf.set_font("Arial",size=15, style='B')
     pdf.set_xy(col1x+109,col1y+85)
     pdf.cell(colw,colh, txt='Invoice Number:',ln=True, align='L' )
     
     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+155,col1y+85)
     pdf.cell(colw,colh, txt=num,ln=True, align='L' )

     pdf.set_font("Arial",size=15, style='B')
     pdf.set_xy(col1x+109,col1y+95)
     pdf.cell(colw,colh, txt='Invoice Date:',ln=True, align='L' )

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+150,col1y+95)
     pdf.cell(colw,colh, txt=ndate,ln=True, align='L' )

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+15,col1y+216)
     pdf.cell(colw,colh, txt='Due Date:',ln=True, align='L' )

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+45,col1y+216)
     pdf.cell(colw,colh, txt=ndue,ln=True, align='L' )


     pdf.set_font("Arial",size=15, style='B')
     pdf.set_xy(col1x+15,col1y+125)
     pdf.cell(colw,colh, txt='Description:',ln=True, align='L' )

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+15,col1y+135)
     pdf.cell(colw,colh, txt=descript,ln=True, align='L')

     pdf.set_font("Arial",size=15, style='B')
     pdf.set_xy(col1x+75,col1y+125)
     pdf.cell(colw,colh, txt='Quantity:',ln=True, align='L' )

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+85,col1y+135)
     pdf.cell(colw,colh, txt=nquantity,ln=True, align='L')

     pdf.set_font("Arial",size=15, style='B')
     pdf.set_xy(col1x+110,col1y+125)
     pdf.cell(colw,colh, txt='Price per Unit:',ln=True, align='L' )

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+120,col1y+135)
     pdf.cell(colw,colh, txt=nPrice,ln=True, align='L')

     pdf.set_font("Arial",size=15, style='B')
     pdf.set_xy(col1x+165,col1y+125)
     pdf.cell(colw,colh, txt='Total:',ln=True, align='L' )

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+164,col1y+135)
     pdf.cell(colw,colh, txt=f'${nTotal}',ln=True, align='L')
     
     pdf.set_line_width(0.5) #set the width of the line
     pdf.line(col1x+10, col1y+135,col1x+180,col1y+135) 


     pdf.set_font("Arial",size=19, style='B')
     pdf.set_xy(col1x+15,col1y+180)
     pdf.cell(colw,colh, txt='Payment Info:',ln=True, align='L' )   

     pdf.set_font("Arial",size=19, style='B')
     pdf.set_xy(col1x+115,col1y+180)
     pdf.cell(colw,colh, txt='Payment Due:',ln=True, align='L' )   

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+15,col1y+192)
     pdf.cell(colw,colh, txt='Account Name:',ln=True, align='L' )    
   
     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+52,col1y+192)
     pdf.cell(colw,colh, txt=name,ln=True, align='L' )

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+15,col1y+200)
     pdf.cell(colw,colh, txt='Account Number:',ln=True, align='L' )      

     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+57,col1y+200)
     pdf.cell(colw,colh, txt=num,ln=True, align='L' )      


     pdf.set_font("Arial",size=15)
     pdf.set_xy(col1x+15,col1y+208)
     pdf.cell(colw,colh, txt='Bank Name:  UAE Bank',ln=True, align='L' )      

     pdf.set_font("Arial",size=19, style='B')
     pdf.set_xy(col1x+129,col1y+195)
     pdf.cell(colw,colh, txt=f'${nTotal}',ln=True, align='L' )      

     #pdf.set_font('Arial', size=15 )
    # pdf.set_xy(col)

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
     pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="60%" height="600px" />'


     #Display the embedded pdf (Markdown helps us use HTML in streamlit)
     st.markdown(pdf_embed,unsafe_allow_html=True)




