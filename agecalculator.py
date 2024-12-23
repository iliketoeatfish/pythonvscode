#Create an age calculator app that can calculate the age of a user, using his year of birth and his current year. 
#Make sure you ask for the name as well

import streamlit as st

name = st.text_input("What is your name?")

currentyear = st.number_input("What is the current year?", 2023)
yearofbirth = st.number_input("What year were you born in?", 1900,2023)

age = currentyear-yearofbirth

if st.button("Check your Age!"):
    st.write("Your name is", name, "and your age is", age)