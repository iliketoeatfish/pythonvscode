import streamlit as st
import pandas as pd

try:
    quizfile = pd.read_csv('quizresults.csv')
except:
    quizfile = pd.DataFrame()

score = 0

st.header(" :rainbow[HOW MUCH DO YOU KNOW ABOUT ME?]")

st.image('https://cdn.pixabay.com/photo/2024/10/31/10/08/quiz-time-9163843_640.jpg')
menu = st.sidebar.selectbox('Menu',['Take quiz','Quiz Result'])

if menu == 'Quiz Results':
    pass


if menu == 'Take quiz':
    name = st.text_input('What is your name?')

    left, center, right = st.columns(3)


    with left:
        st.subheader(" :rainbow[Question 1]")
        st.text('What is my favourite car?')
        q1 = st.radio('Choose your answer',['Choose','Ferrari','Aston Martin','Mclaren'])

        if q1 == 'Ferrari':
            score +=1

        st.subheader(" :rainbow[Question 4]")
        st.text('What is my favourite subject?')
        q4 = st.radio('Choose your answer',['Choose','PE','Maths','English'])

        if q4 == 'PE':
            score +=1

        st.subheader(" :rainbow[Question 7]")
        st.text('What is my favourite basketball team?')
        q7 = st.radio('Choose your answer',['Choose','Lakers','Celtics','Raptors'])

        if q7 == 'Raptors':
            score +=1

        st.subheader(" :rainbow[Question 10]")
        st.text('Which brother is more fun to play with?')
        q10 = st.radio('Choose your answer',['Choose','Ethan','Damian','Both'])

        if q10 == 'Both':
            score +=1










    with center:
        st.subheader(" :rainbow[Question 2]")
        st.text('Who is my favourite footballer?')
        q2 = st.radio('Choose your answer',['Choose','Pirlo','Beckham','Dele Alli'])

        if q2 == 'Delle Alli':
            score += 1 



        st.subheader(" :rainbow[Question 5]")
        st.text('What is my least favourite subject?')
        q5 = st.radio('Choose your answer',['Choose','Science','history','geography'])

        if q5 == 'history':
            score+=1

        st.subheader(" :rainbow[Question 8]")
        st.text('What is my least favourite premier league team?')
        q8 = st.radio('Choose your answer',['Choose','Aston Villa','Crystal palace','Manchester United'])

        if q8 == 'Manchester United':
            score+=1

        st.subheader(" :rainbow[Question 11]")
        st.text('Which country do I live in?')
        q11 = st.radio('Choose your answer',['Choose','Hong Kong','Sweden','Japan'])

        if q11 =='Hong Kong':
            score +=1









    with right:
        st.subheader(" :rainbow[Question 3]")
        st.text('What is my favourite football team?')
        q3 = st.radio('Choose your answer',['Choose','Newcastle','Chelsea','Liverpool'])

        if q3 == 'Newcastle':
            score +=1

        st.subheader(" :rainbow[Question 6]")
        st.text('What is my favouriTe sport?')
        q6 = st.radio('Choose your answer',['Choose','Football','Track and field','Basketball'])

        if q6 == 'Football':
            score += 1 

        st.subheader(" :rainbow[Question 9]")
        st.text('What is my least favourite car?')
        q9 = st.radio('Choose your answer',['Choose','Lambo','Toyota','Ford'])

        if q9 == 'Ford':
            score += 1 

        st.subheader(" :rainbow[Question 12]")
        st.text('Do I go to church?')
        q12 = st.radio('Choose your answer',['Choose','Yes','No','Sometimes'])

        if q12 == 'Yes':
            score += 1 
        

    if st.button('Submit My Quiz'):

        if q1 == 'Choose':
            st.error('Question 1 has not been answered yet')
        if q2 == 'Choose':
            st.error('Question 2 has not been answered yet')
        if q3 == 'Choose':
            st.error('Question 3 has not been answered yet')
        if q4 == 'Choose':
            st.error('Question 4 has not been answered yet')
        if q5 == 'Choose':
            st.error('Question 5 has not been answered yet')
        if q6 == 'Choose':
            st.error('Question 6 has not been answered yet')
        if q7 == 'Choose':
            st.error('Question 7 has not been answered yet')
        if q8 == 'Choose':
            st.error('Question 8 has not been answered yet')
        if q9 == 'Choose':
            st.error('Question 9 has not been answered yet')
        if q10 == 'Choose':
            st.error('Question 10 has not been answered yet')
        if q11 == 'Choose':
            st.error('Question 11 has not been answered yet')
        if q12 == 'Choose':
            st.error('Question 12 has not been answered yet')


        if (q1 == 'Choose' or  q2 == 'Choose' or  q3 == 'Choose' or  q4 == 'Choose' or  q5 == 'Choose' or  q6 == 'Choose' or  q7 == 'Choose' or 
         q8 == 'Choose' or  q9 == 'Choose' or  q10 == 'Choose' or  q11 == 'Choose' or  q12 == 'Choose'):
         st.error("Please answer all questions")

        elif name:
            st.subheader('Thank you for doing the quiz!')
            st.success(f'You got a score of {score} out of 12')
            quizdict = {name:[name],Score:[score]}
            quiztable = pd.DataFrame(quizdict)
            quiztable.to_csv('quizresults.csv',mode'a',header=quizfile.empty,index=false)

        else:
            st.error('I need your name')

        
        

        














