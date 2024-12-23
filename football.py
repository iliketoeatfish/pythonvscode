#Create one dictionary of 3 football players in 2023
#Give us the player name, games played, goals scored, assist made, yellow cards, red cards
#Turn this to a dataframe (table) which is easy to understand


import streamlit as st
import pandas as pd

football = {'Name':['Garnacho','Haaland','Messi'],'Gamesplayed':[18,31,11],'asisstsmade':[2,5,6],'yellowcards':[1,1,0],
'redcards': [0,0,0] }

st.write(football)

footballdataframe = pd.DataFrame(football)
st.dataframe(footballdataframe)
