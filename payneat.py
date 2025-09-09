import streamlit as st

st.set_page_config(layout='wide')

bill = 0

st.title("Nathan's Steakhouse")

st.image('https://cdn.pixabay.com/photo/2018/09/14/11/12/food-3676796_1280.jpg')

st.header('Appetizer')
app1,app2,app3,app4, = st.columns(4)

with app1:
    if st.checkbox('Bread and butter: $40'):
        bill +=40
        st.success("Added to menu")
    if st.checkbox('Wagyu Beef Tartare: $140'):
        bill +=140
        st.success("Added to menu")
with app2:
    if st.checkbox('Chicken Wings: $60'):
        bill +=60
        st.success("Added to menu")
    if st.checkbox('Crispy Smashed Potatoes: $45'):
        bill +=45
        st.success("Added to menu")
with app3:
    if st.checkbox('Salad with pan seared tuna: $90'):
        bill +=90
        st.success("Added to menu")
    if st.checkbox('Brioche Crab melts: $65'):
        bill +=65
        st.success("Added to menu")
with app4:
    if st.checkbox('Fries: $30'):
        bill +=30
        st.success("Added to menu")
    if st.checkbox('Fresh Prawn Cocktail: $85'):
        bill +=85
        st.success("Added to menu")


st.header('Drinks')
d1,d2,d3,d4 = st.columns(4)

with d1:
    if st.checkbox('Apple Juice: $35'):
        bill +=35
        st.success("Added to menu")
    if st.checkbox('Orange Juice: $35'):
        bill +=35
        st.success("Added to menu")


with d2:
    if st.checkbox('Red Wine: $550'):
        bill +=550
        st.success("Added to menu")
    if st.checkbox('White Wine: $550'):
        bill +=550
        st.success("Added to menu")

with d3:
    if st.checkbox('Coke : $25'):
        bill +=25
        st.success("Added to menu")
    if st.checkbox('Sprite: $25'):
        bill +=25
        st.success("Added to menu")   

with d4:
    if st.checkbox('Champagne: $1250'):
        bill +=1250
        st.success("Added to menu")
    if st.checkbox('Beer: $60'):
        bill +=60
        st.success("Added to menu")   


st.header('Main Courses')
m1,m2,m3,m4 = st.columns(4)

with m1:
    if st.checkbox('Wagyu Ribeye : $950'):
        bill +=850
        st.success("Added to menu")
    if st.checkbox('Wagyu Tomahawk: $1300'):
        bill +=1300
        st.success("Added to menu")   


with m2:
    if st.checkbox('Filet Mignon : $850'):
        bill +=850
        st.success("Added to menu")
    if st.checkbox('Wagyu Porterhouse: $1350'):
        bill +=1350
        st.success("Added to menu")


with m3:
    if st.checkbox('NY striploin : $780'):
        bill +=780
        st.success("Added to menu")
    if st.checkbox('T-bone: $1200'):
        bill +=1200
        st.success("Added to menu")


with m4:
    if st.checkbox('Tenderloin : $1050'):
        bill +=1050
        st.success("Added to menu")
    if st.checkbox('Japanese Kobe Beef: 2500'):
        bill +=2500
        st.success("Added to menu")


st.header('Desserts')
d1,d2,d3,d4 = st.columns(4)

with d1:
    if st.checkbox('Matcha Ice cream: 55'):
        bill+=55
        st.success("Added to Menu")
    if st.checkbox('Cherry Sorbet: $65'):
        bill+=65
        st.success("Added to Menu")

with d2:
      if st.checkbox('Homemade French Vanilla Ice cream: 70'):
        bill+=70
        st.success("Added to Menu")
      if st.checkbox('Homemade Strawberry Ice cream: 45'):
        bill+=45
        st.success("Added to Menu")

with d3:
    if st.checkbox('Blueberry Cheesecake: 80'):
        bill+=80
        st.success("Added to menu")
    if st.checkbox('Creme Brule: 95'):
        bill+=95
        st.success("Added to Menu")

with d4:
    if st.checkbox('Raspberry Shortcake: 120'):
        bill+=120
        st.success("Added to Menu")
    if st.checkbox('Sundae: 170')   :
        bill+=170
        st.success("Added to Menu") 



if st.button("Your Bill"):
    st.header(f"Your total bill is ${bill}")
    
