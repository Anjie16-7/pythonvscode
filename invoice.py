import streamlit as st
from fpdf import FPDF
import base64 # convert python binary to printable characters 

st.set_page_config(page_title='Invoice Generator', page_icon="📕",layout="centered", initial_sidebar_state="expanded")
import pandas as pd
csvlink= pd.read_csv('invoice.csv')
menu= st.sidebar.selectbox("Menu", ['Invoice',"Change Details"])
image_url=https://github.com/Anjie16-7/pythonvscode/blob/main/logo.jpg?raw=true
if menu == 'Change Details':
    pw=st.sidebar.text_input("Enter Password",type='password')
    #logo, name, addr, country, bank name, acc name, number,
    if pw=='1234':
        l1,l2,l3 = st.columns([1,2,1])
        with l2:
            logo = st.file_uploader("Change your logo here", type=['jpg','png', 'jpeg'])
            if st.button("Save Image"):
                if logo:
                    with open("logo.jpg",'wb') as writename:
                        writename.write(logo.getbuffer())
                else:
                    st.write("Please upload an image")
                
            left,right = st.columns(2)
        with left:
            cname = st.text_input ("Change company name here")
            ccountry = st.text_input("Change company country here")
            accname = st.text_input ("Change account name here")
    
        with right:
            caddress = st.text_input("Change company address here")
            bankname = st.text_input("Change bank name here")
            accnumber = st.text_input("Change account number here")
        if st.button("Save Changes"):
           # detailsdict={"Name":[cname],"Country":[ccountry],"Account Name":[accname],"Company Address":[caddress],"Bank Name":[bankname],"Account Number":[accnumber]}
            

            
            detailsdict={}
            if cname:
                detailsdict['Name']=[cname]
            else:
                detailsdict['Name']=csvlink['Name'].iloc[0]
            if ccountry:
                detailsdict['Country']=[ccountry]
            else:
                detailsdict['Country']=csvlink['Country'].iloc[0]
            if accname:
                detailsdict['Account Name']=[accname]
            else:
                detailsdict['Account Name']=csvlink['Account Name'].iloc[0]
            if caddress:
                detailsdict['Company Address']=[caddress]
            else:
                detailsdict['Company Address']=csvlink['Company Address'].iloc[0]
            if bankname:
                detailsdict['Bank Name']=[bankname]
            else:
                detailsdict['Bank Name']=csvlink['Bank Name'].iloc[0]
            if accnumber:
                detailsdict['Account Number']=[accnumber]
            else:
                detailsdict['Account Number']=csvlink['Account Number'].iloc[0]
            table = pd.DataFrame(detailsdict)
            table.to_csv('invoice.csv',index=False)
            
            s1,s2,s3=st.columns(3)
            with s1:
                st.success("Details Have Been Changed")
                

            
                

if menu=='Invoice':

    cname2=csvlink["Name"].iloc[0]
    ccountry2=csvlink["Country"].iloc[0]
    caddress2=csvlink["Company Address"].iloc[0]
    bankname2=csvlink["Bank Name"].iloc[0]
    accnumber2=csvlink["Account Number"].iloc[0]
    accname2=csvlink["Account Name"].iloc[0]
    
    st.sidebar.write("OPTIONAL")
    tax = st.sidebar.number_input("Enter tax %",0.0,100.0)
    discount = st.sidebar.number_input("Enter discount %",0.0,100.0)


    col1,col2,col3=st.columns(3)
    with col3:
        st.title("Invoice")
    with col1:
        logo = st.image("logo.jpg",120,120)
    st.write(cname2)
    st.write(ccountry2)
    st.write(caddress2)
    col4,col5=st.columns(2)
    with col4:
        name=st.text_input("Bill to:",placeholder='Customer Name', )
        address= st.text_input('E',placeholder="Email Address",label_visibility= 'collapsed')
    with col5:
        num=st.text_input('Invoice#:', placeholder="Invoice Number")
        date= st.date_input('Invoice Date:')
        day=date.day
        month=date.strftime('%B')
        year=date.year
        date=f'{day} {month} {year}'
        
        
        
        
        due= st.date_input("Due Date:")
        dday=due.day
        dmonth=due.strftime('%B')
        dyear=due.year
        due=f'{day} {month} {year}'

    
    col6,col7,col8,col9=st.columns(4)
    with col6:
        descript= st.text_input('Description', placeholder='Enter Description')
    with col7:
        
        quantity=st.number_input("Quantity",0,100)
    
        
        
    with col8:
        Price= st.number_input("Price per Unit")
        Total= quantity*Price
        tans=(tax/100)*Total
        st.write(f"Tax:",f'${tans:,}')
        
    with col9:    
        show= st.text_input("Total Price",f'${Total:,}')
        dans=(discount/100)*Total
        st.write(f"Discount:",f'${dans:,}')
    st.divider()
    col10, col11=st.columns(2)
    with col10:
        st.subheader("Payment info")
        sname= st.write("Acc Name:",accname2)
        snum= st.write("Acc Number:",accnumber2)
        st.write("Bank Name:",bankname2)
    with col11:
        st.write("Payment Due")
        pdue= Total + tans - dans
        st.header(f'${pdue:,}')
        

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
        pdf.image("logo.jpg",x=col1x, y=col1y, w=45)
        pdf.set_font("Arial", size=21, style='B')

        pdf.set_xy(col1x+140,col1y+15)
        pdf.cell(colw,colh, txt='INVOICE',ln=True,align='L')

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+15,col1y+40)
        pdf.cell(colw,colh, txt=f'{cname2}',ln=True, align='L' )

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+15,col1y+50)
        pdf.cell(colw,colh, txt=f'{caddress2}',ln=True, align='L' )

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+15,col1y+60)
        pdf.cell(colw,colh, txt=f'{ccountry2}',ln=True, align='L' )

        pdf.set_font("Arial",size=15, style='B')
        pdf.set_xy(col1x+15,col1y+85)
        pdf.cell(colw,colh, txt='Bill to:',ln=True, align='L' )


        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+33,col1y+85)
        pdf.cell(colw,colh, txt=f'{name}',ln=True, align='L' )

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+15,col1y+95)
        pdf.cell(colw,colh, txt=f'{address}',ln=True, align='L' )

        pdf.set_font("Arial",size=15, style='B')
        pdf.set_xy(col1x+109,col1y+85)
        pdf.cell(colw,colh, txt='Invoice Number:',ln=True, align='L' )
        
        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+155,col1y+85)
        pdf.cell(colw,colh, txt=f'{num}',ln=True, align='L' )

        pdf.set_font("Arial",size=15, style='B')
        pdf.set_xy(col1x+109,col1y+95)
        pdf.cell(colw,colh, txt='Invoice Date:',ln=True, align='L' )

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+150,col1y+95)
        pdf.cell(colw,colh, txt=f'{date}',ln=True, align='L' )

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+15,col1y+216)
        pdf.cell(colw,colh, txt='Due Date:',ln=True, align='L' )

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+45,col1y+216)
        pdf.cell(colw,colh, txt=f'{due}',ln=True, align='L' )


        pdf.set_font("Arial",size=15, style='B')
        pdf.set_xy(col1x+15,col1y+125)
        pdf.cell(colw,colh, txt='Description:',ln=True, align='L' )

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+15,col1y+135)
        pdf.cell(colw,colh, txt=f'{descript}',ln=True, align='L')

        pdf.set_font("Arial",size=15, style='B')
        pdf.set_xy(col1x+75,col1y+125)
        pdf.cell(colw,colh, txt='Quantity:',ln=True, align='L' )

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+85,col1y+135)
        pdf.cell(colw,colh, txt=f'{quantity}',ln=True, align='L')

        pdf.set_font("Arial",size=15, style='B')
        pdf.set_xy(col1x+110,col1y+125)
        pdf.cell(colw,colh, txt='Price per Unit:',ln=True, align='L' )

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+120,col1y+135)
        pdf.cell(colw,colh, txt=f'${Price:,}',ln=True, align='L')

        pdf.set_font("Arial",size=15, style='B')
        pdf.set_xy(col1x+165,col1y+125)
        pdf.cell(colw,colh, txt='Total:',ln=True, align='L' )

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+164,col1y+135)
        pdf.cell(colw,colh, txt=f'${Total:,}',ln=True, align='L')
        
        pdf.set_line_width(0.5) #set the width of the line
        pdf.line(col1x+15, col1y+135,col1x+180,col1y+135) 


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
        pdf.cell(colw,colh, txt=f'{accnumber2}',ln=True, align='L' )      


        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+15,col1y+208)
        pdf.cell(colw,colh, txt='Bank Name:',ln=True, align='L' )

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+24,col1y+208)
        pdf.cell(colw,colh, txt=f'{bankname2}',ln=True, align='L' )      
        
        pdf.set_font("Arial",size=19, style='B')
        pdf.set_xy(col1x+129,col1y+195)
        pdf.cell(colw,colh, txt=f'${pdue:,}',ln=True, align='L' )      


        pdf.set_font("Arial",size=15, style='B')
        pdf.set_xy(col1x+155,col1y+155)
        pdf.cell(colw,colh, txt="Tax:",ln=True, align='L')

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+166,col1y+155)
        pdf.cell(colw,colh, txt=f'${tans:,}',ln=True, align='L')

        pdf.set_font("Arial",size=15, style='B')
        pdf.set_xy(col1x+155,col1y+162)
        pdf.cell(colw,colh, txt="Discount:",ln=True, align='L')

        pdf.set_font("Arial",size=15)
        pdf.set_xy(col1x+180,col1y+162)
        pdf.cell(colw,colh, txt=f'${dans:,}',ln=True, align='L')

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


  #  if st.button(":blue[View Invoice]"):
        #Write the PDF using base64
   #    pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')


        #Generate the HTML to embed the PDF
  #     pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="60%" height="600px" />'


        #Display the embedded pdf (Markdown helps us use HTML in streamlit)
  #     st.markdown(pdf_embed,unsafe_allow_html=True)
    col1,col2,col3=st.columns(3)
    with col1:
        if name and address and num and date and due and descript and quantity and Price:
            st.download_button(label='Download PDF', data=pdf_data, file_name='aishainvoice.pdf', mime='application/pdf')
        else:
            st.error('Kindly Fill in the boxes')



