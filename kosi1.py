
import streamlit as st #webpage to view your python app
import pandas as pd #used to read, write on CSV files and view as tables




#save the students data in their different categories
#1 dict #1b view as table
#2 csv


#try tells the computer what to do normally and except tells the computer what to do when there's an error


#STEP 1: FIND THE FILE
try:
    #pd please help to find and read this file called ..
    allstudents = pd.read_csv('studentscores2.csv')
except:
    allstudents = pd.DataFrame() #this creates an empty table
#--------------------------

userid="User_"+str(len(allstudents)+1)

menu = st.sidebar.selectbox('menu',['Input Scores','View Scores','Student File'])


if menu == 'Student File':
    find=st.sidebar.text_input("Enter Student ID")
    









if menu == 'View Scores':
    st.table(allstudents)
   
   
if menu == 'Input Scores':




    st.header('Student Data Base')
    name = st.text_input('Enter Student Name:')




    sub1,sub2 = st.columns(2)








    with sub1:
        health = st.number_input('Enter Health score',0,100)
        math = st.number_input('Enter Math Score',0,100)
        eng = st.number_input('Enter English score',0,100)
        art = st.number_input('Enter Art score',0,100)
    with sub2:
        fr = st.number_input('Enter French score:',0,100)
        science = st.number_input('Enter Science score',0,100)
        religion = st.number_input('Enter Religion score',0,100)
        socialStudies = st.number_input('Enter Social Studies score',0,100)








    totalScore = fr + science + religion +  socialStudies + health + math + eng + art








    averageScore = totalScore / 8
    roundAve = round(averageScore,2)
    if roundAve >= 90:
        Grade = ('A+')
    elif roundAve >= 80:
        Grade = ('B+')
    elif roundAve >= 60:
        Grade = ('C-')
    elif roundAve >= 50:
        Grade = ('D')
    else:
        Grade = ('F-')








    if st.button("Submit Student's Grade"):
        st.write(name+"'s grade is ,",Grade,'their average is',roundAve,'and thier total score is',totalScore,".")
       
       #STEP 2: SAVE THE DATA IN A DICTIONARY
        newstudentdict = {"ID":[userid],'Name':[name], "Health":[health], 'Math':[math], 'English':[eng],
                        'Art':[art], 'French':[fr], 'Science':[science], 'Religion':[religion], 'Social Studies':[socialStudies],
                        'Total Score': [totalScore], 'Average Score': [roundAve], 'Grade':[Grade]}
        # st.write(studentdict)
        # st.table(studentdict)
        #pandas please help me convert this dict into a table form


        #STEP 3: CHANGE/CONVERT THIS DICT INTO A TABLE FORM
        newstudent_table = pd.DataFrame(newstudentdict)


        #STEP 4: JOIN THE OLD WITH THE NEW
        jointables = pd.concat([allstudents,newstudent_table],ignore_index=True) #this joins the old and new tables together
       
        #STEP 5: SAVE THE CSV FILE
        jointables.to_csv('studentscores2.csv',index=False)
        #concatenate
       
       
        #st.table(newstudent_table)


