import streamlit as st

name = 'steve'

pickaxe_cost = 80

shield_cost = 30

torch_cost = 15

totalprice = pickaxe_cost + shield_cost + torch_cost

st.write(name,'you bought pickaxe for',pickaxe_cost,'dollars')
st.write(name,'you bought a shield for',pickaxe_cost,'dollars')
st.write(name,'you bought a torch for',torch_cost,'dollars')

st.write('Hi Steve! You spent a total of $',totalprice)