import streamlit as st
import pandas as pd


st.header("Car Dealer Shop")
st.subheader("Enter the new car specifications")


carname = st.text_input("Enter car name")


caryear = st.text_input('Enter the year of the car')


carbrand = st.text_input("Enter the brand of the car")


transmission = st.radio("Enter car transmision",['Automatic','Manual'])


if st.button("Add New Car Specifications"):
    car_dict = {'CarName':[carname],'Caryear':[caryear],'Carbrand':[carbrand]}

    st.write(car_dict)

    car_dataframe = pd.DataFrame(car_dict)
    st.table(car_dataframe)