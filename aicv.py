import streamlit as st

with st.sidebar:
    name = st.text_input('Enter your full name')
    st.divider()
    number = st.text_input('Enter your phone number')
    st.divider()
    address = st.text_input('Enter your home address')
    st.divider()
    if st.toggle('Email (Optional)'):
        email = st.text_input('Enter your email')

    if st.toggle('Photo (Optional)'):
        photo = st.file_uploader('Choose an image type', type=['jpg','jpeg','png'])

    st.divider()
    skills = st.text_area('Enter your key skills',placeholder='Examples: \nPhotography \nVideography \nArts and Craft \nPainting')
    st.divider()
    work = st.text_area('Enter your work experience',placeholder='Examples: \nSydney, Australia: 2010-2019 (Remote) \nBoston, US: 2020-2025')
    st.divider()
    education = st.text_area('Describe education',placeholder='Examples: \nUniversity of Idaho: Class of 2015 \nBritish Columbia: Class of 2019')
    

    
