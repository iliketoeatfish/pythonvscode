
import streamlit as st
import pandas as pd
"""
CLASS ASSESSMENT
1.What is streamlit used for?
2.show 8 ways to display text on streamlit
3.show how to ask for a text on streamlit
4.show how to ask for a number on streamlit
5.create a button on the left column but show the output on the right column
6.create a radio button with a horizontal orientation
7.import an image with a 150*150 size
8. read and dispay a CSV file in python
9.create a toggle option to display any database/dataframe
10.create a dictionary of 5 different cars with 5 attributes (without using a CSV file) 
and convert it to a dataframe/table
"""

st.write("Streamlit is used to show the code on the screen")
st.write(" 1. st.write ")
st.title('2. st.title')
st.header('3. st.header')
st.success('4. st.success')
st.subheader('5. st.subheader')
st.text('6. st.text')
st.error('7. st.error')
st.info('8. st.info')
bird = st.text_input("What is your favourite type of bird? ")
number = st.number_input("What is your favourite number?")
st.image('https://cdn.pixabay.com/photo/2017/09/25/13/12/puppy-2785074_1280.jpg',150)
database = pd.read_csv('scores.csv')
st.dataframe(database)

car_dict = {'brand' : ['ferrari'],'model name':['Laferrari'],'transmission':['automatic'],'year made':['2013'],'price':['million']}
car_dataframe= pd.DataFrame(car_dict)
st.dataframe(car_dict)
st.dataframe(car_dataframe)
