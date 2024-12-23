import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
menu = st.sidebar.selectbox('menu',['register staff','staff database','staff file'])

database = pd.read_csv('employee.csv')


if menu == 'register staff':

    st.header("Register here")
    name, eg = st.columns(2)

    with name:
        fname = st.text_input("Please insert your first name")
    
    with name:
        email = st.text_input("Please insert your email address")
    
    
    with eg:
       lname = st.text_input("Please insert your last name")
    
    with eg:
        gender = st.selectbox('Gender',('male','female'))


    d, j = st.columns(2)

    with d:
        department =  st.selectbox('Department', ('Management', 'Accounting', 'Engineering', 'Human Resources', 'Security', 'Medical', 'Transportation'))
    
    with j:
        Jobtitle = st.selectbox('Job Title',('Board Of Directors', 'Supervisor', 'Senior Staff', 'Junior Staff', 'Paid Intern', 'Unpaid Intern'))

    status, income = st.columns(2)

    with status:
        contract = st.selectbox('Contract status',('Full Time','Part Time'))
    
    with income:
     income = st.number_input('Monthly income', 10000,500000)


    e, d = st.columns(2)

    with e:
        educational = st.selectbox('Educational degree', ('None','Assocaite degree','Bachelor degree','Graduate degree','Professional degree','Doctoral degree'))
    
    with d:
        date = st.date_input("Employement date")

    if st.button("Submit employee data"):
    


        employee_dict = {'First name':[fname], 'Last name':[lname],'Email':[email],'Gender':[gender],'Department':[department],'Contract status':[contract],
    'Monthly income':[income],'Educational degree':[educational],'Employement date':[date]}
        employee_dataframe = pd.DataFrame(employee_dict)
        new_database = pd.concat([database,employee_dataframe], ignore_index=True)
        new_database.to_csv('employee.csv', index=False) 
        st.write("Your data is saved")
     
#add a login to the database page only. no one should view staff database without the password
if menu == 'staff database':
    
    correctpassword = '12345'
    password = st.text_input("Please enter the password", type='password')

    if st.button('Login'):
        if password:
         if password == correctpassword:
            csv = pd.read_csv('employee.csv')
            st.dataframe(csv)
        
         else:
            st.write("The password is incorrect")

        else:
            st.write("There was no password inputed")
    
    


        

     
    





       

    



