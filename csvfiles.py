import streamlit as st
import pandas as pd#help you open and read CSv files then covert into table


# csv files are text files that each data is seperated by a comma(comma seperated values)

st.set_page_config(layout='wide')

df = pd.read_csv('grades.csv') #pd will help read CSV file.

st.dataframe(df) #how the data frame
 