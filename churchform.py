#classwork: create a simple church form that has a name (text), age range (selectbox) and gender (radio) on 3 columns
#then a text area to ask for other additional message

import streamlit as st
import pandas as pd

st.title("Nathan's church form")

c1,c2,c3 = st.columns(3)

with c1:
    name = st.text_input("What is your name?")

with c2:
    age = st.selectbox("Select your age range",['0-15','16-25','26-35','36-45','46-55','56-65','66-75','75+'])

with c3:
    gender = st.radio("Select your gender",['Male','Female'])

message = st.text_area("Leave us a message")

if st.button("Submit"):
    st.subheader("Thanks, we have receieved your information.")

    information = {'Name':[name],'Age':[age],'Gender':[gender],'Message':[message]}

    info_dataframe = pd.DataFrame(information)
    st.table(info_dataframe)
