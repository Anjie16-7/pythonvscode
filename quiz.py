# create an app for your friends on how much they know you or know something or general quiz
# asks the user to enter his/her name on the questionnaire page
# the questionnaire page can be arranged in 3 or more columns (use your own ideas(-radio - selecbox))
# a button under after all to submit and this checks the right questions and add the scores and save the user score under the user name

# the other page plots the charts of all users who answered and shows their scores

import streamlit as st 
import pandas as pd 

menu= st.sidebar.selectbox("Quizzes",["Personal","Trivia"])

if menu== "Personal":

    try:
        link=pd.read_csv("quiz.csv")
    except:
        link=pd.DataFrame()

    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'


    if 'name' not in st.session_state:
        st.session_state.name = ''
        st.rerun()



    def home():
        st.title("Quiz")
        name= st.text_input("Enter Name")
        st.session_state.name = name

        if st.pills("",["Begin"]):
            if name:
                link.loc[0,st.session_state.name]=0
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'qf1'
                st.rerun()

            else:
                st.error("Must Enter A Name")

    
    def qf1():
        
        
        st.subheader('Question 1')
        st.write('')
        q1 = st.selectbox('What is my favorite ice cream flavour', ["Choose",'Plain Vanilla', 'Fudgy Chocolate','Minty Flavor','Strawberry'])
        if st.button('Next Question'):
            if q1 == 'Choose':
                st.error("Enter an answer")
            elif q1=="Fudgy Chocolate":
            
                
                link.loc[0, st.session_state.name ]+=1
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'qf2'
                st.rerun()
            else:
                link.loc[0, st.session_state.name]+= 0
                
                st.session_state.current_page = 'qf2'
                st.rerun()
    def qf2():
        st.subheader('Question 2')
        st.write('')
        q2 = st.selectbox('What is my favorite childhood animal', ["Choose",'Dog','Cat','Dolphin','Otter'])
        if st.button('Next Question'):
            if q2 == 'Choose':
                st.error("Enter an answer")
            elif q2=="Dolphin":
                link.loc[0, st.session_state.name ]+=1
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'qf3'
                st.rerun()
            else:
                link.loc[0, st.session_state.name ]+=0
                link.to_csv("quiz.csv",index=False)
                
                st.session_state.current_page = 'qf3'
                st.rerun()
    def qf3():            
        st.subheader('Question 3')
        st.write('')
        q3 = st.selectbox('What is my irrational fear', ["Choose",'Spiders', 'Bodies Of Water','Heights','Germs'])
        if st.button('Next Question'):
            if q3 == 'Choose':
                st.error("Enter an answer")
            elif q3=="Bodies Of Water":
                link.loc[0, st.session_state.name ]+=1
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'qf4'
                st.rerun()
            else:
                link.loc[0, st.session_state.name ]+=0 
                link.to_csv("quiz.csv",index=False)
                
                st.session_state.current_page = 'qf4'
                st.rerun()
    def qf4():
        st.subheader('Question 4')
        st.write('')
        q4 = st.selectbox('What was my favorite colour as a kid', ["Choose",'Pink', 'Black','White','Blue'])
        if st.button('Next Question'):
            if q4 == 'Choose':
                st.error("Enter an answer")
            elif q4=="Black":
                link.loc[0, st.session_state.name ]+=1
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'qf5'
                st.rerun()
            else:
                link.loc[0, st.session_state.name ]+=0
                link.to_csv("quiz.csv",index=False)
                
                st.session_state.current_page = 'qf5'
                st.rerun()

    def qf5():
        st.subheader('Question 5')
        st.write('')
        q5 = st.selectbox('What was my first best friends name', ["Choose",'Kosi', 'Joy','Hannah','Nicolette'])
        if st.button('Next Question'):
            if q5 == 'Choose':
                st.error("Enter an answer")
            elif q5=="Nicolette":
                link.loc[0, st.session_state.name ]+=1
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'qf6'
                st.rerun()
            else:
                link.loc[0, st.session_state.name ]+=0
                link.to_csv("quiz.csv",index=False)
                
                st.session_state.current_page = 'qf6'
                st.rerun()

    def qf6():
        st.subheader('Question 6')
        st.write('')
        q6 = st.selectbox('What is my favorite animal', ["Choose",'Cat', 'Hamster','Dog','Bunny'])
        if st.button('Next Question'):
            if q6 == 'Choose':
                st.error("Enter an answer")
            elif q6=="Dog":
                link.loc[0, st.session_state.name ]+=1
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'qf7'
                st.rerun()
            else:
                link.loc[0, st.session_state.name ]+=0
                link.to_csv("quiz.csv",index=False)
                
                st.session_state.current_page = 'qf7'
                st.rerun()

    def qf7():
        st.subheader('Question 7')
        st.write('')
        q7 = st.selectbox('Favorite series', ["Choose",'Big Bang Theory', 'Call the Midwife','The Crown','Friends'])
        if st.button('Next Question'):
            if q7 == 'Choose':
                st.error("Enter an answer")
            elif q7=="Friends":
                link.loc[0, st.session_state.name ]+=1
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'qf8'
                st.rerun()
            else:
                link.loc[0, st.session_state.name ]+=0
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'qf8'
                st.rerun()

    def qf8():
        st.subheader('Question 8')
        st.write('')
        q8 = st.selectbox('College Of my dreams', ["Choose",'Chapel Hill', 'NC State','MIT','GeorgiaTech'])
        if st.button('Next Question'):
            if q8 == 'Choose':
                st.error("Enter an answer")
            elif q8=="Chapel Hill":
                link.loc[0, st.session_state.name ]+=1
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'qf9'
                st.rerun()
            else:
                link.loc[0, st.session_state.name ]+=0
                link.to_csv("quiz.csv",index=False)
                
                st.session_state.current_page = 'qf9'
                st.rerun()


    def qf9():
        st.subheader('Question 9')
        st.write('')
        q9 = st.selectbox('How I like my eggs best', ["Choose",'Scrambled', 'Boiled (Yolk)','Boiled (White)','Omelette'])
        if st.button('Next Question'):
            if q9 == 'Choose':
                st.error("Enter an answer")
            elif q9=="Scrambled":
                link.loc[0, st.session_state.name ]+=1
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'qf0'
                st.rerun()
            else:
                link.loc[0, st.session_state.name ]+=0
                link.to_csv("quiz.csv",index=False)
                
                st.session_state.current_page = 'qf0'
                st.rerun()

    def qf0():
        st.subheader('Question 10')
        st.write('')
        q0 = st.selectbox('What is my favorite flower', ["Choose",'Lilies', 'Roses','Daffodil','Sunflowers'])
        if st.button('Next Question'):
            if q0 == 'Choose':
                st.error("Enter an answer")
            elif q0=="Lilies":
                link.loc[0, st.session_state.name ]+=1
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'done'
                st.rerun()
            else:
                link.loc[0, st.session_state.name ]+=0
                link.to_csv("quiz.csv",index=False)
                st.session_state.current_page = 'done'
                st.rerun()

    def done():

        v1,v2,v3=st.columns([1,3,1])
        with v2:
            st.title("Complete!")
        s1,s2= st.columns(2)
        with s1:
            
            if st.button("Play Again."):
                st.session_state.current_page = 'home'
                st.rerun()
        with s2:
            if st.button("Show Results"):
                global results   
                results= link[st.session_state.name].iloc[0]
             
                
                st.success(f"{st.session_state.name} got {results} out of 10 for the personal quiz.")






    if st.session_state.current_page == 'home':
        home()
    

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
    elif st.session_state.current_page == 'done':
        done()




if menu== "Trivia":

    try:
        link2=pd.read_csv("trivia.csv")
    except:
        link2=pd.DataFrame()
    b1,b2,b3=st.columns([1,3,1])
    with b2:
        st.title ("Let's begin!")

    tname=st.text_input("Enter name:")
    y= st.pills('',["Go!"])
    if y:
        if tname:
                    link2.loc[0, tname ]=0
                    link2.to_csv("trivia.csv",index=False)
                    st.divider()
                    s1,s2=st.columns(2)
                    with s1:
                        t1=st.selectbox("When was Nato formed",["Choose","1945","1914","1949","1946"],)
                        t2= st.selectbox("What is the male camel known as?",["Choose","Bull","Camel","Tom","Buck"])
                        t3= st.selectbox("The middle colour in a rainbow",["Choose","Yellow","Blue","Indigo","Green"])
                        t4=st.selectbox("Feijoada is the national dish of which South American country",["Choose","Argentina","Peru","Brazil","Venezuela"])
                        t5=st.selectbox("Name of the first dog in space",["Choose","Robbie","Laika","Sue","Charlie"])
                    with s2:
                        t6= st.selectbox("Only Country with a Bible on its national flag",["Choose","Chad","Dominican Republic","Brazil","Philippines"])
                        t7=st.selectbox("What is papaphobia a fear of?",["Choose","Butterflies","Liquids","Food","The Pope"])
                        t8= st.selectbox("What animal character lives on Skull Island",["Choose","Winnie the Poo","Popeye","Paddington","Mushu","King Kong"])
                        t9= st.selectbox("In mythology,Sirens is a mixture of a woman and what",["Choose","Fish", "Horse","Bird","Cat"])
                        t0= st.selectbox("Ronald Regan middle name",["Choose","Wilson","Johnson","Warren","Donald"])

                    if t1=="Choose" or t2=="Choose" or t3=="Choose" or t4=="Choose" or t5=="Choose" or t6=="Choose" or t7=="Choose" or t8=="Choose" or t9=="Choose" or t0=="Choose":
                        st.error("Need to select an answer for all the questions")
                    else:
                        if st.button("Submit All"):                    
                            if t1=="1945":
                                link2.loc[0, tname ]+=1
                                link2.to_csv("trivia.csv",index=False)

                            else:
                                link2.loc[0, tname ]+=0
                                link2.to_csv("trivia.csv",index=False)
                                

                            if t2=="Bull":
                                link2.loc[0, tname ]+=1
                                link2.to_csv("trivia.csv",index=False)
                                
                            else:
                                link2.loc[0, tname ]+=0
                                link2.to_csv("trivia.csv",index=False)
                                

                            if t3=="Green":
                                link2.loc[0, tname ]+=1
                                link2.to_csv("trivia.csv",index=False)
                                
                            else:
                                link2.loc[0, tname ]+=0
                                link2.to_csv("trivia.csv",index=False)
                                
                            
                            if t4=="Brazil":
                                link2.loc[0, tname ]+=1
                                link2.to_csv("trivia.csv",index=False)
                                
                            else:
                                link2.loc[0, tname ]+=0
                                link2.to_csv("trivia.csv",index=False)
                                
                            
                            if t5=="Laika":
                                link2.loc[0, tname ]+=1
                                link2.to_csv("trivia.csv",index=False)
                                
                            else:
                                link2.loc[0, tname ]+=0
                                link2.to_csv("trivia.csv",index=False)
                                
                            
                            if t6=="Dominican Rebuplic":
                                link2.loc[0, tname ]+=1
                                link2.to_csv("trivia.csv",index=False)
                                
                            else:
                                link2.loc[0, tname]+=0
                                link2.to_csv("trivia.csv",index=False)
                                

                            if t7=="The Pope":
                                link2.loc[0, tname ]+=1
                                link2.to_csv("trivia.csv",index=False)
                                
                            else:
                                link2.loc[0, tname ]+=0
                                link2.to_csv("trivia.csv",index=False)
                                

                            if t8=="King Kong":
                                link2.loc[0, tname]+=1
                                link2.to_csv("trivia.csv",index=False)
                                
                            else:
                                link2.loc[0, tname ]+=0
                                link2.to_csv("trivia.csv",index=False)
                            

                            if t9=="Bird":
                                link2.loc[0, tname]+=1
                                link2.to_csv("trivia.csv",index=False)
                                
                            else:
                                link2.loc[0, tname ]+=0
                                link2.to_csv("trivia.csv",index=False)
                                

                            if t0=="Wilson":
                                link2.loc[0, tname ]+=1
                                link2.to_csv("trivia.csv",index=False)
                                
                            else:
                                link2.loc[0, tname ]+=0
                                link2.to_csv("trivia.csv",index=False)
                                st.error("Choose an Answer")
                            results2=link2[tname].iloc[0] 
                            st.success (f"You got {results2} out of 10 correct.")
                            
