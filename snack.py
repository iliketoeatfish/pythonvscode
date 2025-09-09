import streamlit as st
import pandas as pd


st.set_page_config(layout='wide')

menu = st.sidebar('Menu',['Enter Weekly Scores','Submit student scores'])

st.write('Enter students name and score for the week')

if menu == 'Enter Weekly Scores':

    python = st.number_input('Python score is')
    web = st.number_input('Web Developement score is')
    robotics = st.number_input('Robotics score is')
    solving = st.number_input('Problem solving score is')

total =  python+web+robotics+solving 

if menu == 'Submit student scores':

    avg = total/4

    st.write('Your final score is:',avg)

    if avg >= 90:
        st.write('Congratulations! you got the platinum badge')

    elif avg >= 80:
        st.write('Well done! you got the gold badge')

    elif avg >= 70:
        st.write("Good Job you got a silver badge")

    elif avg >= 60:
        st.write('Nice job you got a bronze medal')

    elif avg < 60:
        st.write('Nice try, keep on working hard!')





