import streamlit as st
import pandas as pd

left , right = st.columns(2)

with left:
    name = st.text_input('What is your name?')

with right: 
    roll = st.text_input("What is your roll number")

with left:
    present = st.number_nput("How many days present?")

with right:
    absent = st.number_input = ("How many days absent")

attendance_dict = {'Name':[name],'Roll':[roll],'Present':[present],'Absent':[absent]}

