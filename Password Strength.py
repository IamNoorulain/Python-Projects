import streamlit as st
import re

st.set_page_config(page_title="SecurePass", page_icon="🔒", layout="centered")
st.title("🔒 SecurePass Strength Meter")

with st.expander("How it works"):
    st.write("""
        ► 1 point for length ≥ 8  
        ► 1 point each for uppercase, lowercase, digit, special character  
        Score 0–2: Weak 🚩  
        Score 3: Moderate ⚠️  
        Score 4–5: Strong ✅
    """)

pwd = st.text_input("Enter password", type="password")
if pwd:
    score = sum([
        len(pwd) >= 8,
        bool(re.search(r"[A-Z]", pwd)),
        bool(re.search(r"[a-z]", pwd)),
        bool(re.search(r"\d", pwd)),
        bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", pwd))
    ])
    levels = {0: "🚩 Too weak", 1: "🚩 Too weak", 2: "🚩 Too weak",
              3: "⚠️ Moderate", 4: "✅ Strong", 5: "✅ Strong"}
    bar = st.progress(score / 5)
    st.write(f"Score: **{score}/5** — {levels[score]}")
