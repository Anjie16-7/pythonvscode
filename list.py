# classwork:
# create a list.py file
# -tell us what a list is in python
# -create an example of a list and display all the list items in python
# -give 3 examples of how to use a list in streamlit (radio, selectbox, sidebar)

# a group of items separated by a comma
import streamlit as st
colour=['Pink','Red','Yellow','White']
st.write(colour)

desserts= st.selectbox('Desserts', ['Chocolate','Ice cream','Pizza'])

drinks=st.radio('Drinks',['Pepsi','Coke','Fanta'])
st.write('You choose',drinks)

menu = st.sidebar.selectbox('Meals',['Pizza','Chicken','Pasta'])




