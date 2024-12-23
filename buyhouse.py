#TEST 1
#write a python program for house buyers
#create a menu for the buy house page and the house database page
#Ask them for their name
#ask them for their yearly salary
#if they earn below 100000 they can buy or rent an apartment
#If the earn between 100000-500,000 they can buy a bungalow
#If the earn between >500,000-1,000,000 they can buy a duplex
#If the earn between >1,000,000-5,000,000 they can buy a manshion
#if the earn above 5000000 they can buy an estate
#create a database to to store and view their answers and display in another customer section

import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title("Buy a house")

menu = st.sidebar.selectbox('Menu',['House','Database'])

if menu == 'House':
    name = st.text_input("What is your name?")
    salary = st.number_input("What is your yearly salary?")
