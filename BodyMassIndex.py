import streamlit as st




st.title('Adult BODY MASS INDEX')

st.header("Height")

h1,h2  = st.columns(2)

with h1:
    meters = st.number_input("How many meters are you?") 

with h2:
    Inches = st.number_input("How many inches are you?")

st.header("Weight")
w1, w2 = st.columns(2)

with w1:
    kg = st.number_input("How much kilograms do you weigh?")

with w2:
    pounds = st.number_input("How much pounds do you weigh?")


if st.button("Check BMI"):
    height = meters**2
    weight = kg
    bmi=weight/height


    if bmi < 18.5:
        st.write("You are underweight")
    elif bmi >= 18.5 and bmi < 25:
        st.write("You have a healthy weight")
    elif bmi >= 25.0 and bmi <=29.9:
        st.write("You are Overweight")

    else:
        st.write("You are obese")
        
    st.write(bmi)



