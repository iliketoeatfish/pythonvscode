import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
st.title('Private school application form')
database = pd.read_csv('schoolapp.csv')

menu = st.sidebar.selectbox('Menu',['Application','Database'])


if menu == 'Application':
    c1,c2 = st.columns(2)
    with c1:
        parentname = st.text_input('Parent/guardian name')
        age = st.number_input("How old is your child?",0)
    with c2:
        plastname = st.text_input('Parent/guardian last name')
        gender = st.radio('Child gender',["Male",'Female'],horizontal=True)
    c3,c4 = st.columns(2)
    with c3:
        cname = st.text_input("Child name:")
    with c4:
        clname = st.text_input("Child last name:")
    
    school = st.text_input('The school that he comes from:')
    haddress = st.text_input('Home Address',placeholder='Street Address')
    line2 = st.text_input('Street address line 2',placeholder='Street Address line 2',label_visibility='collapsed')
    
    c5, c6 = st.columns(2)
    with c5:
        city = st.text_input("City",placeholder='City',label_visibility='collapsed')
        zipcode = st.text_input('zipcode',placeholder='Postal/Zipcode',label_visibility='collapsed')
    with c6:
        region = st.text_input('Region',placeholder='Region',label_visibility='collapsed')
        country = st.text_input('country',placeholder='Country',label_visibility='collapsed')
    
    pnumber = st.text_input('Phone Number',placeholder='Phone number')


    if st.button('Submit'): 
        st.subheader("Thanks we recieved your application to our school")
        school_dict = {'Parent FirstName':[parentname],'Parent Lastname':[plastname],'Gender':[gender],'Child Firstname':[cname],'Child Lastname':[clname],
        'School':[school],'Home Address':[haddress],'Line2':[line2],'City':[city],'Zipcode':[zipcode],'Region':[region],
        'Country':[country],'Phone Number':[pnumber]}
        school_dataframe = pd.DataFrame(school_dict)
        new_database = pd.concat([database,school_dataframe])
        new_database.to_csv('schoolapp.csv')


