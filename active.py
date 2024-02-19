import streamlit as st
num1 = st.number_input("Enter the Number1:")
num2 = st.number_input("Enter the Number2:")
if st.button("Add"):
    st.write(f"#The total is {num1+num2}")
    st.snow()