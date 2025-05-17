import streamlit as st

st.title("BMI Calculator")

gender = st.selectbox("Select your gender:", ["Male", "Female"])
age = st.number_input("Enter your age:", min_value=1)

weight = st.number_input("Enter your weight (kg):", min_value=1.0)
height = st.number_input("Enter your height (kg):", min_value=1.0)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 😟"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight 😊"
    elif 25 <= bmi < 29.9:
        return "Overweight 😐"
    else:
        return "Obese 😟"
    
def bmi_calcutor(weight, height):
    bmi = weight / ((height)**2)
    
    return round(bmi, 2)


if st.button("Calculate"):
    try:
        bmi = bmi_calcutor(weight, height)
        category = get_bmi_category(bmi)

        st.success(f"Your BMI is {bmi}")
        st.info(f"Category: {category}")
        st.markdown(f"**Gender:** {gender} &nbsp;&nbsp; **Age:** {age}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
