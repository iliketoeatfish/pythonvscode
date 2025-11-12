#homework: create a simple church form with 3 columns
#1 that has a name (text), type their age and choose their gender (st.radio) on 3 columns]

# decide member class with these categories: (Kids(3-12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) --== if block

# when you click on submit button:
#Make sure you group members in different category based on their age
#write this welcome [name], you will be in the [churchclass] class
#your message has been received
#show the user message here

import streamlit as st

st.title('Church form')

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input('what is your name?')

with col2:
    age = st.number_input ('what is your age?',0)

with col3:
    gender = st.radio('what is your gender',['Male','Female'])

if age >= 3 and age <= 12:
    group = 'kids class'

elif age >= 13 and age <= 19:
    group = 'teens class'

elif age >= 20 and age <= 35:
    group = 'youth class'

elif age >= 36 and age <= 64:
    group = 'adult class'

elif age >= 65:
    group = 'elder class'

if st.button('See your church class'):
    st.header(f'Welcome {name} Your class is going to be the {group}')


