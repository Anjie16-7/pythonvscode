import streamlit as st
import pandas as pd
import plotly.express as px
import time
import base64
import datetime



from fpdf import FPDF
try:
        link=pd.read_csv("medical.csv")
except:
        link=pd.DataFrame()

menu= st.sidebar.selectbox("Menu",["Quiz","Leaderboard","Check Result"])

if menu=="Quiz":
    

    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'main'


    if 'name' not in st.session_state:
        st.session_state.name = ''
        st.rerun()

    if 'answers' not in st.session_state:
        st.session_state.answers= {}
        
    
    if 'scores' not in st.session_state:
        st.session_state.scores={}
    
   
   
    def countdown():
        with st.spinner("Loading Next Page",show_time=True):
            time.sleep(3)
     

    def main():
        st.title(f":blue[Medical Trivia]")
        st.write()
        st.write("Welcome! Today we are going to test our medical skills with a series of questions!")
        name= st.text_input("Enter Name:")
        st.session_state.name = name
        st.write()
        if name:
            
            
            st.write("Ready?")
            but=st.pills("",["Let's Go"])
            if but: 
                x = datetime.datetime.now()
                st.session_state.date=x.strftime("%d-%b-%Y")
                link.loc[0,st.session_state.name]=0
                link.to_csv("medical.csv",index=False)
                st.session_state.current_page = 'qf1'
                st.rerun()
        else :
            w1,w2=st.columns(2)
            with w1:
                st.error("Need to enter a name")
    def qf1():
        st.subheader('Question 1')
        st.write('')

        c1,c2=st.columns(2)
        with c2:
            try:
                st.info(f"Current answer: {st.session_state.answers['1']}")
            except:
                st.info("Current answer:None")
                


        
        

        with c1:
            q1 = st.selectbox('What is my main job of the heart?', ["Choose",'Pumping blood', 'Digesting Food','Storing Energy','Breathing Air'])
            if st.button('Next Question'):
                
                st.session_state.answers['1']=q1
                
                
                
                
                
                if q1 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q1']=0         
                    st.session_state.current_page = 'qf2'
                    st.rerun()


                elif q1=="Pumping blood":
                    st.session_state.scores['q1'] = 1
                    st.session_state.current_page = 'qf2'
                    st.rerun()
                else:
                    st.session_state.scores['q1']=0
                    st.session_state.current_page = 'qf2'
                    st.rerun()
    def qf2():

        c3,c4=st.columns(2)
        with c4: 
            try:
                st.info(f"Current answer: {st.session_state.answers['2']}")
            except:
                st.info("Current answer:None")


        with c3:
            st.subheader('Question 2')
            st.write('')
            q2 = st.selectbox('What do vaccines help protect you from?', ["Choose",'Common Cold', 'Diseases like measles and flu','Cuts and bruises','None Of the Above'])
            l1,l2=st.columns(2)
            with l2:
                n=st.button('Next Question')
            with l1:
                p=st.button('Previous Question')

            if n :
                
                st.session_state.answers['2']=q2
                if q2 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q2']=0
                

                    st.session_state.current_page = 'qf3'
                    st.rerun()
                elif q2=="Diseases like measles and flu":
                
                    
                    st.session_state.scores['q2']=1
                    st.session_state.current_page = 'qf3'
                    st.rerun()
                else:
                    st.session_state.scores['q2']=0
                
                    st.session_state.current_page = 'qf3'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf1'
                st.rerun()
    def qf3():

            c5,c6=st.columns(2)
            with c6: 
                try:
                    st.info(f"Current answer: {st.session_state.answers['3']}")
                except:
                    st.info("Current answer:None")


            with c5:
                st.subheader('Question 3')
                st.write('')
                q3 = st.selectbox('Why is it important to wash your hands?', ["Choose",'To smell nice', ' To prevent getting sick','To look clean','None Of the Above'])
                l1,l2=st.columns(2)
                with l2:
                    n=st.button('Next Question')
                with l1:
                    p=st.button('Previous Question')

                if n :
                   
                    st.session_state.answers['3']=q3 
                    if q3 == 'Choose':
                        st.error("Enter an answer")
                        st.session_state.scores['q3']=0
                        
                        st.session_state.current_page = 'qf4'
                        st.rerun()
                    elif q3==" To prevent getting sick":
                    
                        
                        st.session_state.scores['q3']=1
                        
                        st.session_state.current_page = 'qf4'
                        st.rerun()
                    else:
                        st.session_state.scores['q3']=0
                        
                        st.session_state.current_page = 'qf4'
                        st.rerun()
                if p:
                    st.session_state.current_page = 'qf2'
                    st.rerun()
    def qf4():
        st.subheader('Question 4')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['4']}")
            except:
                st.info("Current answer:None")
        with c7:
            q4 = st.selectbox('What should you do if you have a fever?', ["Choose",' Tell an adult and rest', 'Eat a lot of candy','Stay up late','Go outside'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['4']=q4
                if q4 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q4']=0
                            
                    st.session_state.current_page = 'qf5'
                    st.rerun()
                elif q4==" Tell an adult and rest":
                
                    
                    st.session_state.scores['q4']=1
                            
                    st.session_state.current_page = 'qf5'
                    st.rerun()
                else:

                    st.session_state.scores['q4']=0
                            
                    st.session_state.current_page = 'qf5'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf3'
                st.rerun()
    def qf5():
        st.subheader('Question 5')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['5']}")
            except:
                st.info("Current answer:None")
        with c7:
            q5=st.selectbox('What does a doctor do?', ["Choose",'Fix Cars', ' Teach maths',' Help people stay healthy','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['5']=q5
                if q5 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q5']=0
                            
                    st.session_state.current_page = 'qf6'
                    st.rerun()
                elif q5==" Help people stay healthy":
                
                    
                    st.session_state.scores['q5']=1
                            
                    st.session_state.current_page = 'qf6'
                    st.rerun()
                else:

                    st.session_state.scores['q5']=0
                            
                    st.session_state.current_page = 'qf6'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf4'
                st.rerun()
    def qf6():
        st.subheader('Question 6')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['6']}")
            except:
                st.info("Current answer:None")
        with c7:
            q6=st.selectbox("What's a healthy snack?", ["Choose",'Candy', ' Chips','Soda',' Fruits and vegetables'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['6']=q6
                if q6 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q6']=0
                            
                    st.session_state.current_page = 'qf7'
                    st.rerun()
                elif q6==" Fruits and vegetables":
                
                    
                    st.session_state.scores['q6']=1
                            
                    st.session_state.current_page = 'qf7'
                    st.rerun()
                else:

                    st.session_state.scores['q6']=0
                            
                    st.session_state.current_page = 'qf7'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf5'
                st.rerun()
    def qf7():
        st.subheader('Question 7')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['7']}")
            except:
                st.info("Current answer:None")
        with c7:
            q7=st.selectbox("What's the meaning of being allergic to something?", ["Choose",'You like it a lot', 'Your body reacts to it','You can not eat it','None Of The Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['7']=q7
                if q7 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q7']=0
                            
                    st.session_state.current_page = 'qf8'
                    st.rerun()
                elif q7=="Your body reacts to it":
                
                    
                    st.session_state.scores['q7']=1
                            
                    st.session_state.current_page = 'qf8'
                    st.rerun()
                else:

                    st.session_state.scores['q7']=0
                            
                    st.session_state.current_page = 'qf8'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf6'
                st.rerun()
    def qf8():
        st.subheader('Question 8')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['8']}")
            except:
                st.info("Current answer:None")
        with c7:
            q8=st.selectbox('What should you do if you get a cut?', ["Choose",'Ignore It', 'Wash it and put a bandage on it','Show it to your friends','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['8']=q8
                if q8 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q8']=0
                            
                    st.session_state.current_page = 'qf9'
                    st.rerun()
                elif q8=='Wash it and put a bandage on it':
                
                    
                    st.session_state.scores['q8']=1
                            
                    st.session_state.current_page = 'qf9'
                    st.rerun()
                else:

                    
                    st.session_state.scores['q8']=0
                            
                    st.session_state.current_page = 'qf9'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf7'
                st.rerun()
    def qf9():
        st.subheader('Question 9')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['9']}")
            except:
                st.info("Current answer:None")
        with c7:
            q9=st.selectbox('Why is it important to eat breakfast?', ["Choose",'It gives you energy for school', ' You can skip it','It is the best meal of the day','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['9']=q9
                if q9 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q9']=0
                            
                    st.session_state.current_page = 'qf0'
                    st.rerun()
                elif q9=='It gives you energy for school':
                
                    
                    st.session_state.scores['q9']=1
                            
                    st.session_state.current_page = 'qf0'
                    st.rerun()
                else:

                    st.session_state.scores['q9']=0
                            
                    st.session_state.current_page = 'qf0'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf8'
                st.rerun()
    def qf0():
        st.subheader('Question 10')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['10']}")
            except:
                st.info("Current answer:None")
        with c7:
            q0=st.selectbox('What is one way to keep your bones strong?', ["Choose",'Eating Junk', 'Drinking milk or eating dairy','Avoiding exercise','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['10']=q0
                if q0 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q0']=0
                            
                    st.session_state.current_page = 'qf11'
                    st.rerun()
                elif q0=='Drinking milk or eating dairy':
                
                    
                    st.session_state.scores['q0']=1
                            
                    st.session_state.current_page = 'qf11'
                    st.rerun()
                else:

                    st.session_state.scores['q0']=0
                            
                    st.session_state.current_page = 'qf11'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf9'
                st.rerun()
    def qf11():
        st.subheader('Question 11')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['11']}")
            except:
                st.info("Current answer:None")
        with c7:
            q11=st.selectbox('What is the purpose of first aid?', ["Choose",'To give immediate care in emergencies', 'To make food',' To help with homework','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
               
                st.session_state.answers['11']=q11
                if q11 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q11']=0
                            
                    st.session_state.current_page = 'qf12'
                    st.rerun()
                elif q11=='To give immediate care in emergencies':
                
                    
                    st.session_state.scores['q11']=1
                            
                    st.session_state.current_page = 'qf12'
                    st.rerun()
                else:

                    st.session_state.scores['q11']=0
                            
                    st.session_state.current_page = 'qf12'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf0'
                st.rerun()
    def qf12():
        st.subheader('Question 12')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['12']}")
            except:
                st.info("Current answer:None")
        with c7:
            q12=st.selectbox('What can help you breathe better when you’re sick?', ["Choose",'Eating Ice cream', 'Running around','Drinking warm fluids','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['12']=q12
                if q12 == 'Choose':
                    st.error("Enter an answer")
                    
                    st.session_state.scores['q12']=0
                            
                    st.session_state.current_page = 'qf13'
                    st.rerun()
                elif q12=='Drinking warm fluids':
                
                    
                    st.session_state.scores['q12']=1
                            
                    st.session_state.current_page = 'qf13'
                    st.rerun()
                else:

                    st.session_state.scores['q12']=0
                            
                    st.session_state.current_page = 'qf13'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf11'
                st.rerun()
    def qf13():
        st.subheader('Question 13')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['13']}")
            except:
                st.info("Current answer:None")
        with c7:
            q13=st.selectbox('What is a common symptom of a cold?', ["Choose",'Runny Nose', 'Happy Thoughts','Dancing','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
             
                st.session_state.answers['13']=q13
                if q13 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q13']=0
                            
                    st.session_state.current_page = 'qf14'
                    st.rerun()
                elif q13=='Runny Nose':
                
                    
                    st.session_state.scores['q13']=1
                            
                    st.session_state.current_page = 'qf14'
                    st.rerun()
                else:

                    st.session_state.scores['q13']=0
                            
                    st.session_state.current_page = 'qf14'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf12'
                st.rerun()
    def qf14():
        st.subheader('Question 14')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['14']}")
            except:
                st.info("Current answer:None")
        with c7:
            q14=st.selectbox('Why should you cover your mouth when you cough?', ["Choose",'It is fun', 'No one can ssee inside your mouth','Prevent spreading sickness','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
               
                st.session_state.answers['14']=q14
                if q14 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q14']=0
                            
                    st.session_state.current_page = 'qf15'
                    st.rerun()
                elif q14=='Prevent spreading sickness':
                
                    
                    st.session_state.scores['q14']=1
                            
                    st.session_state.current_page = 'qf15'
                    st.rerun()
                else:

                    st.session_state.scores['q14']=0
                            
                    st.session_state.current_page = 'qf15'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf13'
                st.rerun()
    def qf15():
        st.subheader('Question 15')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['15']}")
            except:
                st.info("Current answer:None")
        with c7:
            q15=st.selectbox('What is a safe way to exercise?', ["Choose",'Jumping on the bed', 'Playing sports or riding a bike','Sitting all day','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['15']=q15
                if q15 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q15']=0
                            
                    st.session_state.current_page = 'qf16'
                    st.rerun()
                elif q15=='Playing sports or riding a bike':
                
                    
                    st.session_state.scores['q15']=1
                            
                    st.session_state.current_page = 'qf16'
                    st.rerun()
                else:

                    st.session_state.scores['q15']=0
                            
                    st.session_state.current_page = 'qf16'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf14'
                st.rerun()
    def qf16():
        st.subheader('Question 16')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['16']}")
            except:
                st.info("Current answer:None")
        with c7:
            q16=st.selectbox('What does a dentist check?', ["Choose",'Your Hair', ' Your eyes','Your teeth','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['16']=q16
                if q16 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q16']=0
                            
                    st.session_state.current_page = 'qf17'
                    st.rerun()
                elif q16=='Your teeth':
                
                    
                    st.session_state.scores['q16']=1
                            
                    st.session_state.current_page = 'qf17'
                    st.rerun()
                else:

                    st.session_state.scores['q16']=0
                            
                    st.session_state.current_page = 'qf17'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf15'
                st.rerun()
    def qf17():
        st.subheader('Question 17')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['17']}")
            except:
                st.info("Current answer:None")
        with c7:
            q17=st.selectbox('What should you do if you feel dizzy?', ["Choose",'Sit down and tell an adult', 'Eat candy','Keep running','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                st.session_state.answers['17']=q17
                if q17 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q17']=0
                            
                    st.session_state.current_page = 'qf18'
                    st.rerun()
                elif q17=='Sit down and tell an adult':
                
                    
                    st.session_state.scores['q17']=1
                            
                    st.session_state.current_page = 'qf18'
                    st.rerun()
                else:

                    st.session_state.scores['q17']=0
                            
                    st.session_state.current_page = 'qf18'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf16'
                st.rerun()
    def qf18():
        st.subheader('Question 18')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['18']}")
            except:
                st.info("Current answer:None")
        with c7:
            q18=st.selectbox('What is the main function of your lungs?', ["Choose",'To pump blood', 'To digest food','To help you breathe','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['18']=q18
                if q18 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q18']=0
                            
                    st.session_state.current_page = 'qf19'
                    st.rerun()
                elif q18=='To pump blood':
                
                    
                    st.session_state.scores['q18']=1
                            
                    st.session_state.current_page = 'qf19'
                    st.rerun()
                else:

                    st.session_state.scores['q18']=0
                            
                    st.session_state.current_page = 'qf19'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf17'
                st.rerun()
    def qf19():
        st.subheader('Question 19')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['19']}")
            except:
                st.info("Current answer:None")
        with c7:
            q19=st.selectbox('What can help you stay healthy during cold and flu season?', ["Choose",'Washing hands frequently', 'Eat sweets','Skipping sleep','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Next Question')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['19']=q19
                if q19 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q19']=0
                            
                    st.session_state.current_page = 'qf20'
                    st.rerun()
                elif q19=='Washing hands frequently':
                
                    
                    st.session_state.scores['q19']=1
                            
                    st.session_state.current_page = 'qf20'
                    st.rerun()
                else:

                    st.session_state.scores['q19']=0
                            
                    st.session_state.current_page = 'qf20'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf18'
                st.rerun()
    def qf20():
        st.subheader('Question 20')
        st.write('')
        c7,c8=st.columns(2)
        with c8: 
            try:
                st.info(f"Current answer: {st.session_state.answers['20']}")
            except:
                st.info("Current answer:None")
        with c7:
            q20=st.selectbox('What does it mean if someone has a headache?', ["Choose",'They want to play', ' They are happy','They might need rest or water','None Of the Above'])
            f1,f2=st.columns(2)
            with f2:
                n=st.button('Summary')
            with f1:
                p=st.button('Previous Question')
            
            if n :
                
                st.session_state.answers['20']=q20
                if q20 == 'Choose':
                    st.error("Enter an answer")
                    st.session_state.scores['q20']=0
                            
                    st.session_state.current_page = 'done'
                    st.rerun()
                elif q20=='They might need rest or water':
                
                    
                    st.session_state.scores['q20']=1
                            
                    st.session_state.current_page = 'done'
                    st.rerun()
                else:

                    st.session_state.scores['q20']=0
                            
                    st.session_state.current_page = 'done'
                    st.rerun()
            if p:
                st.session_state.current_page = 'qf19'
                st.rerun()
    def done():
        st.title("Summary")
        for key,value in st.session_state.answers.items():
            if value == 'Choose':
               st.write('Question',key,'has not been answered yet')
               
        f1,f2=st.columns(2)
        with f2:
            n=st.button('Submit')
        with f1:
            p=st.button('Previous Question')
            
        if n :
            st.session_state.current_page= 'end'
            st.rerun()
            
            
            

        if p:
            st.session_state.current_page = 'qf20'
            st.rerun()

    def end():
        st.title("Completed")
        total= sum(st.session_state.scores.values())
        
        
        

        

        per= str(total/20 *100)
        st.write(st.session_state.name,"got ",per,"%")
        link.loc[0,st.session_state.name]=total
        link.to_csv("medical.csv",index=False)
        
        def generate_pdf():
            pdf=FPDF(orientation="landscape",format='A4')
            pdf.add_page()
            url='certificate.png'

            col1x = 20
            col1y = 25
            colw=50
            colh=40

            pdf.image(url, x=0, y=0, w=270, h=150)

            pdf.set_font("Times",size=60)
            pdf.set_xy(col1x+100,col1y+16)
            pdf.cell(colw,colh+35, txt=f'{st.session_state.name}',ln=True, align='L' ) 

            pdf.set_font("Times",size=35)
            pdf.set_xy(col1x+40,col1y+40)
            pdf.cell(colw,colh+45, txt=f'{total}/20',ln=True, align='L' ) 

            pdf.set_font("Times",size=35)
            pdf.set_xy(col1x+140,col1y+40)
            pdf.cell(colw,colh+45, txt=f'{st.session_state.date}',ln=True, align='L' ) 

            

            pdf_file = 'medical.pdf'
            pdf.output(pdf_file)
            return pdf_file

            

                
                

        pdf_func = generate_pdf()
        with open(pdf_func, 'rb') as binary:
            pdf_data = binary.read()
        
        w1,w2= st.columns([4,1])

        with w1:

            if st.button("View Cetificate"):
                pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')
                pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="60%" height="600px" />'
                st.markdown(pdf_embed,unsafe_allow_html=True)
        
        with w2:
            st.download_button(label='Download PDF', data=pdf_data, file_name='certificate.pdf', mime='application/pdf')






        sta=st.button("Home Page")
        if sta:
            st.session_state.current_page="main"
            st.rerun()



    if st.session_state.current_page == 'main':
        main()
    elif st.session_state.current_page == 'qf1':
        qf1()
    elif st.session_state.current_page == 'qf2':
        qf2()
    elif st.session_state.current_page == 'qf3':
        qf3()
    elif st.session_state.current_page == 'qf3':
        qf3()
    elif st.session_state.current_page == 'qf4':
        qf4()
    elif st.session_state.current_page == 'qf5':
        qf5()
    elif st.session_state.current_page == 'qf6':
        qf6()
    elif st.session_state.current_page == 'qf7':
        qf7()
    elif st.session_state.current_page == 'qf8':
        qf8()
    elif st.session_state.current_page == 'qf9':
        qf9()
    elif st.session_state.current_page == 'qf0':
        qf0()
    elif st.session_state.current_page== 'qf11':
        qf11()
    elif st.session_state.current_page == 'qf12':
        qf12()
    elif st.session_state.current_page == 'qf13':
        qf13()
    elif st.session_state.current_page == 'qf14':
        qf14()
    elif st.session_state.current_page == 'qf15':
        qf15()
    elif st.session_state.current_page == 'qf16':
        qf16()
    elif st.session_state.current_page == 'qf17':
        qf17()
    elif st.session_state.current_page == 'qf18':
        qf18()
    elif st.session_state.current_page == 'qf19':
        qf19()
    elif st.session_state.current_page=='qf20':
        qf20()
    elif st.session_state.current_page == 'done':
        done()
    elif st.session_state.current_page =="end":
        end()
melt = link.melt(var_name='Name', value_name='Score Out Of 20')
if menu=="Leaderboard":
    st.title("Leadership Board")
    st.write()
    st.write("Who Is In The Lead?")
    c1,c2,c3=st.columns([1,3,1])
    with c2:
        cho=st.selectbox("Display Format", ["Pie Chart","Table"])
    
    
    if cho== "Table":
        chart= px.bar(melt, x= "Name",y="Score Out Of 20")
        st.plotly_chart(chart)
    if cho=="Pie Chart":
        pie=px.pie(melt, names="Name",values="Score Out Of 20")
        st.plotly_chart(pie)

        
            

        