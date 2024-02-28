import streamlit as st


#concatenating is simply merging two data or datasets together
# , makes a space
number1 = '5'
number2 = '5'
st.write(number1+number2)

firstname = 'Jason'
lastname = 'Akin'
st.write(firstname + lastname)

oldmovies = ['spiderman returns', 'catwoman']
newmovies = ['the lost kingdom','the tribe of Judah']
st.write(oldmovies,newmovies) #prints on list then other
st.write(oldmovies + newmovies)#adds all items to one list
