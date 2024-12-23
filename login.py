#create a login feature to read the scores database

import streamlit as st
import pandas as pd

correctpassword = 'Nathan12345'


password = st.text_input("Please enter the password",type='password')

if st.button("Login"):
    if password:
        if password == correctpassword:
            csv = pd.read_csv('scores.csv')
            st.dataframe(csv)

        else:
            st.write("The password is incorrect")
   
    else:
        st.write("There is no password inputed")



