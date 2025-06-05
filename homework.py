import streamlit as st

tank_name = input("What's the name of your tank? ")

water_level = float(input("How many liters of water are in the tank? "))

tank_capacity = float(input("How many liters can the tank hold in total? "))

if tank_capacity == 0:
    print(f"Error: Tank capacity cannot be zero. Please check the input values for {tank_name}.")
else:
    fill_percentage = (water_level / tank_capacity)