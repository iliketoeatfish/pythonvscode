import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title("CAR")

name = st.text_input("The name of the car is: ")
brand = st.text_input("The brand of the car is: ")
color = st.text_input("The colour of the car is:")

car_dict = {'Name':[name],'Brand':[brand],'Color':[color]}

st.write(car_dict)

car_dataframe = pd.DataFrame(car_dict)
st.table(car_dataframe)