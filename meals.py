import streamlit as st
st.set_page_config(layout="wide")
# -Add title==
#Add a restaurant picture==
# -shows them the food selections
# -After they choose/select their meals, show them the total amount
# -Ask a question if you want to share the bill with others #use checkbox
# -if yes, then ask how many people want to share the bill
# -Then show the amount each person must contribute to pay the bill

#meals, drinks, fruits, snacks

st.title("McDonalds")
st.image("https://cdn.pixabay.com/photo/2018/02/26/18/55/coffee-3183752_1280.jpg")
st.header("Choose your delights")


selectmenu = st.sidebar.selectbox('Select a menu category', ['meals', 'drinks', 'snacks'])
bill=0

if selectmenu == 'drinks':
    st.subheader("Drinks")
    
    drinks1, drinks2, drinks3 =st.columns(3)
    with drinks1:
        if st.checkbox("Pepsi-$5"):
            st.success("Added to menu")
            bill+=5
        if st.checkbox("Sprite-$6"):
            st.success("Added to menu")
            bill+=6

    with drinks2:
        if st.checkbox("Coke-$7"):
            st.success("Added to menu")
            bill+=7
        if st.checkbox("Diet Coke-$8"):
            st.success("Added to menu")
            bill+=8

    with drinks3:
        if st.checkbox("Fanta-$4"):
            st.success("Added to menu")
            bill+=4
        if st.checkbox("Mirinda-$3"):
            st.success("Added to menu")
            bill+=3

elif selectmenu==('meals'):
    st.subheader("Meals")
    meal1,meal2,meal3=st.columns(3)
    with meal1:
        if st.checkbox("Pizza-$30"):
            st.success('Added to menu')
            bill+=30
        if st.checkbox("Salad-$20"):
            st.success('Added to menu')
            bill+=20

    with meal2:
        if st.checkbox("Pasta with chicken-$50"):
            st.success("Added to menu")
            bill+=50
        if st.checkbox("Spagetti with meatballs-$55"):
            st.success('Added to menu')
            bill+=55

    with meal3:
        if st.checkbox("Fries and nuggets-$40"):
            st.success("Added to menu")
            bill+=40
        if st.checkbox("Lamb chops-$45"):
            st.success('Added to menu')
            bill+=45

elif selectmenu==('snacks'):
 st.subheader("Snacks")
 sn1,sn2,sn3=st.columns(3)

 with sn1:
            if st.checkbox("Cookies-$10"):
                st.success("Added to menu")
                bill+=10
            if st.checkbox("Brownies-$17"):
                st.success('Added to menu')
                bill+=17
 with sn2:
            if st.checkbox("Ice cream(vanilla)-$8"):
                st.success("Added to menu")
                bill+=8
            if st.checkbox("Donuts-$20"):
                st.success('Added to menu')
                bill+=20
 with sn3:
            if st.checkbox("Cake-$20"):
                st.success("Added to menu")
                bill+=20
            if st.checkbox("Biscuits-$7"):
                st.success('Added to menu')
                bill+=7
                
                
                
                
                
if st.button("Check bill"):
      st.write("Your total bill is:$",bill)

bill1,bill2,bill3=st.columns(3)
with bill1:
     if st.checkbox("Would you like to share the bill?:"):
         people= st.slider("How many: ",2,50)
         perbill=bill/people
         st.write("Bill per person:$",perbill)