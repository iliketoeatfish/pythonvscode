import streamlit as st
import pandas as pd

try: #create csv and write variables by itself
    allattendance = pd.read_csv('attendance.csv')

except:
    allattendance = pd.DataFrame() #create an empty dataframe

menu = st.sidebar.selectbox('Menu',['Attendance','Show attendance'])
left , right = st.columns(2)

if menu == 'Attendance':
    with left:
        name = st.text_input('What is your name?')

    with right: 
        roll = st.text_input("What is your roll number")

    with left:
        present = st.number_input("How many days present?",0)

    with right:
        absent = st.number_input("How many days absent",0)

    if st.button('See your attendance'):

        attendance_dict = {'Name':[name],'Roll':[roll],'Present':[present],'Absent':[absent]}

        st.write(attendance_dict)

        attendance_dataframe = pd.DataFrame(attendance_dict)
        st.table(attendance_dataframe)

        attendancejoin = pd.concat([allattendance,attendance_dataframe],ignore_index=True)
        attendancejoin.to_csv('attendance.csv',index=False)

if menu == 'Show attendance':
    st.table(allattendance)
    