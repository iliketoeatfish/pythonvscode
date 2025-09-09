import streamlit as st
import pandas as pd

try:
    fruitfile = pd.read_csv('fruitfile.csv')

except:
    fruitfile = pd.DataFrame()

menu = st.sidebar.selectbox('Menu',['Input Purchase','View Purchases'])

st.title("Mr Tee's Fruit Market")

fruits = ['apple','banana','mango','orange','grapes','watermelon','pawpaw','pear','avocado','pineapple']


fruit = st.selectbox('Pick a fruit you would like to buy',fruits)

sold = st.number_input('How mant fruits did you sell?',0)

if st.button('Save sales'):
    st.write('You sold',sold,fruit,'today')

    fruitdict = {'Fruit':[fruit],'Sold':[sold]}
    fruittable = pd.DataFrame(fruitdict)
    fruitjoin = pd.concat([fruitfile,fruittable],ignore_index=True)
    fruitjoin.to_csv('fruitfile.csv',index=False)









