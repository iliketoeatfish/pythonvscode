import streamlit as st
import pandas as pd

#Test:
#Create a simple python program that
#-create a menu for student details and students database
#-Ask for student name on the left column and their age on the right column
#-create a submit button
#- save this in a csv file
#show the dataframe in database page 

database = pd.read_csv('testname.csv')
st.dataframe(database)

name = st.text_input("My name is: ")


age = st.text_input("My age is: ")



if st.button("Save"):
    st.header(f"Your name is {name} and your age is {age}")

    student_dict = {'Name':[name], "Age":[age]}
    student_dataframe = pd.DataFrame(student_dict)
    st.dataframe(student_dataframe)
    new_database = pd.concat([database,student_dataframe], ignore_index=True)
    new_database.to_csv('testname.csv', index=False)