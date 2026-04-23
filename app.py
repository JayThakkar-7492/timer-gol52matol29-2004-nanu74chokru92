import streamlit as st
from datetime import date
import pandas as pd
import requests
from streamlit_lottie import st_lottie

# --- CONFIGURATION ---
TARGET_DATE = date(2026, 5, 1)
TITLE = "Milte hain bahut jaldi!🫶"
VALID_USER = "Nanugolu"
VALID_PASS = "2201200403092004"

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Animation link for Fireworks
lottie_fireworks = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_t2qe3v1v.json")

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if st.session_state["authenticated"]:
        return True
    
    st.title("🔒 Private Access")
    user_input = st.text_input("User ID")
    pass_input = st.text_input("Password", type="password")
    if st.button("Login"):
        if user_input == VALID_USER and pass_input == VALID_PASS:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Invalid User ID or Password")
    return False

def show_timer():
    st.set_page_config(page_title="Countdown", layout="centered")
    
    # Fireworks animation at the top
    st_lottie(lottie_fireworks, height=200, key="fireworks")

    st.markdown("""
        <style>
        .timer-card {
            background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
            padding: 40px;
            border-radius: 25px;
            color: #4a4a4a;
            text-align: center;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
        }
        .days-number { font-size: 80px; font-weight: 800; color: #ff5e62; }
        </style>
    """, unsafe_allow_html=True)

    today = pd.Timestamp.now(tz='Asia/Kolkata').date()
    delta = (TARGET_DATE - today).days

    st.markdown(f"""
        <div class="timer-card">
            <h1>{TITLE}</h1>
            <p class="days-number">{max(0, delta)}</p>
            <p>days left until {TARGET_DATE.strftime('%B %d, %Y')}</p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    if check_password():
        show_timer()
