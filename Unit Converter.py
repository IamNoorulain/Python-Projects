import streamlit as st

st.set_page_config(page_title="Pro Unit Converter", page_icon="🔄", layout="centered")

with st.container():
    st.title("🔄 Pro Unit Converter")
    st.markdown("Convert between length, temperature, and weight units with ease.")

with st.sidebar:
    st.header("Settings")
    precision = st.slider("Decimal precision", 0, 5, 2)

value = st.number_input("Value to convert", min_value=0.0, format="%f")
conversion = st.selectbox("Conversion type", [
    "Kilometers → Miles",
    "Miles → Kilometers",
    "Celsius → Fahrenheit",
    "Fahrenheit → Celsius",
    "Kilograms → Pounds",
    "Pounds → Kilograms"
])

# Compute result
factors = {
    "Kilometers → Miles": lambda x: x * 0.621371,
    "Miles → Kilometers": lambda x: x / 0.621371,
    "Celsius → Fahrenheit": lambda x: (x * 9/5) + 32,
    "Fahrenheit → Celsius": lambda x: (x - 32) * 5/9,
    "Kilograms → Pounds": lambda x: x * 2.20462,
    "Pounds → Kilograms": lambda x: x / 2.20462,
}

result = factors[conversion](value)
st.success(f"Result: **{round(result, precision)}**")
