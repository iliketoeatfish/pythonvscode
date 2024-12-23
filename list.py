
import streamlit as st


#classwork
#1 what is a list?
#2 mention 2 uses of a list
#3 give an example of a list and display it on streamlit
#4 give 3 ways of using a list in streamlit and tell us the function of each method you use

# A list is when you put data in a [] and is seperated with a comma.
# A list is used to store data.

fruit = ['Apple','orange', 'cherry','watermelon']
st.write (fruit)


menu = st.sidebar.selectbox('Menu',['Jewllery store','About us'])

colour = st.selectbox('choose your colour',['Red','green','yellow','blue',2015])

pets = st.selectbox('choose your favourite pet',['dog','cat','hamster','fish','parrott'])

bmw = {'brand name': 'BMW S series', 'country': 'Germany', 'year': 2015, 'transmission':'automatic'}

st.write(bmw)




ferrari = {'brand name': 'Laferrari','country':'Italy','year':2013, 'transmission':'automatic', 'price':'3million'}
st.write(ferrari)