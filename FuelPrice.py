import streamlit as st
import pandas as pd

"""
Classwork 1:
A fuel station sells a litre of fuel for 20$. Create a program in Python to ask how many litres people want to get and then tell them the total price

classwork 2:
save in a csv file how many litres was bought and the total price of the litres for record keeping
"""

database = pd.read_csv('fuel.csv')
st.dataframe(database)

litreprice = 20
st.write("The cost for a litre is", litreprice)

litre = st.number_input("How many litres of fuel do you want to buy?")

totalprice = litre*litreprice

if st.button("Totalprice"):
 st.write("The total price is", totalprice)


litre_dict = {'Litre':[litre], 'Totalprice':[totalprice]}
fuel_dataframe = pd.DataFrame(litre_dict)
new_database = pd.concat([database, fuel_dataframe], ignore_index=True)
new_database.to_csv('fuel.csv', index=False)