#Create a program with streamlit that accepts user input for their name and age. Use this application to accredit whether or not user is eligible to vote.
#Minimum age for voting is 9.
#Ensure you make use of image and an accredit button to display user’s eligibility.
import streamlit as st

st.title('Voting for new senior prefect.')
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR1Pe1jDgcxfKo8irs8jQl8W_orA8Y3UYWWVHZ7gIuPQ&s')

name = st.text_input('What is your name?')
age = st.number_input('How old are you?',1)

if st.button('accredit'):

    if age > 9:
        st.write('Hi',name, 'you are eligible to vote')
    else:
        st.write('Sorry',name, 'you are not eligible to vote')



