# SIMPLE TYPE
#create a simple church age range database

#This will get the name, age, gender of the church member


#Make sure you group members in different category based on their age 
# (Kids(3- 12), Teens(13-19), Youth(20-35), Adult(36-64), Elders(65+) )

import streamlit as st

name = st.text_input("My name is :")
gender = st.text_input("My gender is :")
age = st.number_input("My age is :")



if age >= 65:
    st.write("You are an elder")

if (age >= 36 and age <=64):
    st.write("Your are an adult")

if age >= 20 and age <= 35:
    st.write("You are a youth")


