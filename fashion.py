import streamlit as st

st.set_page_config(layout='wide')

bill = 0

# A fashion app 
# -title
# -image
# -categories
# Men's Fashion

# Women's Fashion

# Children's Fashion

# (each category must havedifferent types of unique items and the prices like shirts
# (long sleeves,short, round neck, polo etc), boxers, trousers, shoes, bags etc)



menu = st.sidebar.selectbox('Menu',['Fashion Store','About us'])

if menu == 'Fashion Store':
    st.title('Welcome to Fashion Store')
    st.image('https://media.istockphoto.com/id/1414692808/photo/sustainable-shopping.webp?b=1&s=612x612&w=0&k=20&c=qDBhwm76EwdEIeMBplMkGkFAnmImHk-T0aRroBjPmaw=')


    st.header("Mens Fashion")
    mf1,mf2,mf3,mf4 = st.columns(4)
    with mf1:
        if st.checkbox('Hat: $750'):
            bill+=250
            st.success("Added to Menu")
        if st.checkbox('Headband: $350'):
            bill+=250
            st.success("Added to Menu")
    
    with mf2:
        if st.checkbox('Tie: $850'):
            bill+=850
            st.success("Added to Menu")
        if st.checkbox('Cufflinks: $650'):
            bill+=240
            st.success("Added to Menu")
    
    with mf3:
        if st.checkbox(' Long Shirt: $2950'):
            bill+=1250
            st.success("Added to Menu")
        if st.checkbox(' Trousers: $1650'):
            bill+=1250
            st.success("Added to Menu")
    
    with mf4:
        if st.checkbox('Shirt: $970'):
            bill+=950
            st.success("Added to Menu")
        if st.checkbox('Short Pants: $890'):
            bill+=250
            st.success("Added to Menu")
        
   
    st.header("Womens Fashion")
    wf1,wf2,wf3,wf4 = st.columns(4)

with wf1:
        if st.checkbox('Hairtie: $370'):
            bill+=370
            st.success("Added to Menu")
        if st.checkbox('Hairclip: $390'):
            bill+=390
            st.success("Added to Menu")
        
with wf2:
    if st.checkbox('Gucci Bag:$95000'):
        bill+=95000
        st.success("Added to Menu")
    if st.checkbox('LV bag: $100,000'):
        bill+=100000
        st.success("Added to Menu")
with wf3:
    if st.checkbox('White dress: $5000'):
        bill+=5000
        st.success("Added to Menu")
with wf3:
    if st.checkbox('Skirt: $2500'):
        bill+=2500
        st.success("Added to Menu")
with wf4:
    if st.checkbox('High heels:$6000'):
        bill+=6000
        st.success("Added to Menu")
    if st.checkbox('Jacket: $4500'):
        bill+=4500
        st.success("Added to Menu")
 
     
st.header("Childrens Fashion")
cf1,cf2,cf3,cf4 = st.columns(4)

with cf1:
    if st.checkbox('Hat: $290'):
        bill+=290
        st.success("Added to Menu")
    if st.checkbox('Earings: $690'):
        bill+=690
        st.success("Added to Menu")

with cf2:
    if st.checkbox('Shirt: $999'):
        bill+=999
        st.success("Added to Menu")
    if st.checkbox('Trousers: $690'):
        bill+=690
        st.success("Added to Menu")

with cf3:
    if st.checkbox('Short Pants: $790'):
        bill+=790
        st.success("Added to Menu")
    if st.checkbox('Tee-shirt: $800'):
        bill+=800
        st.success("Added to Menu")
with cf4:
    if st.checkbox('Shoes: $950'):
        bill+=950
        st.success("Added to Menu")
    if st.checkbox('Socks: $300'):
        bill+=300
        st.success("Added to Menu")

 
 
if menu == 'About us':
    st.title('Welcome to about us')


if st.button("Your bill"):
    st.header(f"Your total bill is ${bill}")