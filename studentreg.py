import streamlit as st 
import pandas as pd






try:
    link= pd.read_csv("studentreg.csv")
except:
    link = pd.DataFrame()
    

#Parent info
#-parent name
#-relationship
#-parent contact

#-Parent email
#-address

userid="User_"+str(len(link)+1)

menu= st.sidebar.selectbox("Menu",["Register",'View Profile'])

if menu=="Register":
    st.title("Student Registration Form")
    q1,q2,q3=st.columns(3)
    with q2:
        st.subheader("Student Info:")
    st.divider()
    col1,col2=st.columns(2)
    with col1:
        name= st.text_input("Enter full name:")
        grade=st.selectbox("Enter Grade:",["First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth"])
        

    with col2:
        dob=st.text_input("Enter Date Of Birth:")
        email=st.text_input("Enter email address:")

    gen1,gen2,gen3=st.columns(3)
    with gen2:
        gen=st.radio("Enter Gender",["Male","Female"],horizontal=True)
 
    pic= st.file_uploader("Upload student's picture here",["jpg","jpeg","png"])
    if pic:
        st.image(pic)

    w1,w2,w3=st.columns(3)
    with w2:
        st.subheader("Parent Info")
    st.divider()
    ss1,ss2= st.columns(2)
    with ss1:
        pname=st.text_input("Enter Parent Name:")
        relations=st.text_input("Relationship with the Student:")
    with ss2:
        num= st.text_input("Phone Number:")
        pemail= st.text_input("Email Address:")
    address=st.text_input("Full Address:")


    if st.button("Submit Student Registration"):
        dict= {"ID":userid,"Student Name":[name],"Grade":[grade],"Date Of Birth":[dob],"Student Email":[email],"Gender":[gen],"Parent Name":[pname],"Relationship":[relations],"Number":[num],"Parent Email":[pemail],"Address":[address]}
        table= pd.DataFrame(dict)
        tab2= pd.concat([link,table], ignore_index= True)
        tab2.to_csv("studentreg.csv",index=False)
        if pic:
            with open (f'{userid}.png','wb') as writepic:
                writepic.write (pic.getbuffer())
            st.success("Image has been saved and data has been stored.")
        else:
            st.error("Need to upload image")

if menu=="View Profile":
    offpass="12345" 
    username= st.sidebar.text_input("Enter ID")
    password= st.sidebar.text_input("Enter Password")
    if st.sidebar.button("View Student Profile"):
        if password==offpass:
            if username:
                find= link[link["ID"].str.lower()==username.lower()]
                cc1,cc2,cc3=st.columns([1,3,1])
                with cc2:
                    st.title("Student Profile")
                gid=find["ID"].iloc[0]
                gname=find['Student Name'].iloc[0]
                ggrade=find['Grade'].iloc[0]
                gdob=find['Date Of Birth'].iloc[0]
                gsemail=find['Student Email'].iloc[0]
                ggender=find['Gender'].iloc[0]
                gpname=find['Parent Name'].iloc[0]
                grelations=find['Relationship'].iloc[0]
                gnum=find['Number'].iloc[0]
                gpemail=find['Parent Email'].iloc[0]
                gaddress=find['Address'].iloc[0]
                st.write("")
                st.write("")
                v1,v2,v3=st.columns([1,2,1])
                with v2:
                    st.header(gname)
                with v3:
                    st.image(f'{gid}.png')
                st.divider()
                s1,s2=st.columns(2)
                with s1:
                    st.subheader("Student Information")
                    st.write("Name:",gname)
                    st.write("Grade:",ggrade)
                    st.write("Date Of Birth:",gdob)
                    st.write("Student's Email:",gsemail)
                    st.write("Gender:",ggender)
                with s2:
                    st.subheader("Parent Information")
                    st.write("Parent's Name:",gpname)
                    st.write("Phone Number:",gnum)
                    st.write("Email:",gpemail)
                    st.write("Address:",gaddress)

                

                


