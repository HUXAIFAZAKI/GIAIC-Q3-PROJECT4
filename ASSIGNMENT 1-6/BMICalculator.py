import streamlit as st
import pandas as pd

st.title("BMI Calculator")

weight = st.number_input("Enter your weight in kg")
height = st.number_input("Enter your height in cm")

bmi = 0

if(height == 0 and weight == 0):
  st.write("Please enter a valid height")
else:
  bmi = weight / ((height/100)**2)
  st.write(f"Your BMI is {bmi:.2f}")

if bmi < 18.5:
  st.write("You are underweight")
elif bmi < 25:
  st.write("You are normal weight")
elif bmi < 30:
  st.write("You are overweight")
else:
  st.write("You are obese")
  st.write("You should see a doctor")

st.title("BMI Table")

df = pd.DataFrame({
  "BMI Category": ["Underweight", "Normal weight", "Overweight", "Obese"],
  "BMI Range": ["<18.5", "18.5-25", "25-30", ">30"]
})

st.write(df)
