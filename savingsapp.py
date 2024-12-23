import streamlit as st

"""
Classwork 1
Create a python program for daily savings for a user, add up all his savings from sunday to saturday
"""
sunday = st.number_input("How much do you save on Sunday?")
monday = st.number_input("How much do you save on Monday?")
tuesday = st.number_input("How much do you save on Tuesday?")
wednesday = st.number_input("How much do you save on Wednesday?")
thursday = st.number_input("How much do you save on Thursday?")
friday = st.number_input("How much do you save on Friday?")
saturday = st.number_input("How much do you want to save on Saturday")

totalsavings = sunday+monday+tuesday+wednesday+thursday+friday+saturday

if st.button("Total savings"):
 st.write("You have", totalsavings, "money saved from sunday to saturday")