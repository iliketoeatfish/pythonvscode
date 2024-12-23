import streamlit as st
import pandas as pd

# Create a student scores database which can 
#  -get the name
#  -4 subjects
#  -calculate the average
#  -calculate the grade (A,B,C,D,E,F)


st.set_page_config(layout='wide')


database = pd.read_csv('scores.csv')
st.dataframe(database)


name = st.text_input("My name is: ")

left , right = st.columns(2)

with left:
    PE = st.number_input("My PE grade is :" ,0,100)
    Science = st.number_input("My Science grade is: ",0,100)

with right:
    Maths = st.number_input("My math grades are :",0,100)
    English = st.number_input("My english grade is :",0,100)

totalscore = PE+Science+Maths+English
average = totalscore/4

if average >= 90:
    grade = 'A+'

elif average >= 80:
    grade = "A"

elif average  >= 70:
    grade = "B"

elif average  >= 60:
    grade = "C"

elif average  >= 50:
    grade = "D"

elif average < 50:
    grade = 'F'


if st.button("Submit Students Scores"):
    st.header(f"Your average is {average} grade: {grade} ")


#this is the dictionary
    student_dict = {'Name':[name],'Maths':[Maths],'English':[English],
                    'Science':[Science],'Physical Ed':[PE],'Total':[totalscore],  'Average':[average],'Grade':[grade]}
 #pandas convert the dict into a table.
    student_dataframe = pd.DataFrame(student_dict)
    new_database = pd.concat([database,student_dataframe], ignore_index=True)
    new_database.to_csv('scores.csv', index=False)

    