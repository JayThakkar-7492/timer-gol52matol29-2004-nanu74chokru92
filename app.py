import streamlit as st
from datetime import date
import pandas as pd  # Necessary for the India Timezone adjustment

# --- CONFIGURATION ---
# The target date and the specific title you requested
TARGET_DATE = date(2026, 5, 1)
TITLE = "Milte hain bahut jaldi!🫶"

# Your specific credentials
VALID_USER = "Nanugolu"
VALID_PASS = "2201200403092004"

def check_password():
    """Handles the secure login gate."""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    # If already logged in, skip the login screen
    if st.session_state["authenticated"]:
        return True

    # Login UI
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
    """The colorful interface of your countdown timer."""
    # Page setup
    st.set_page_config(page_title="Countdown", layout="centered")
    
    # Custom CSS for the colorful UI
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
        .title { font-size: 28px; font-weight: bold; margin-bottom: 20px; }
        .days-number { font-size: 90px; font-weight: 800; color: #ff5e62; }
        .label { font-size: 20px; }
        </style>
    """, unsafe_allow_html=True)

    # DYNAMIC TIMEZONE LOGIC: Fetches 'today' specifically for India
    today = pd.Timestamp.now(tz='Asia/Kolkata').date()
    delta = (TARGET_DATE - today).days

    # The HTML/CSS for the colorful card
    st.markdown(f"""
        <div class="timer-card">
            <div class="title">{TITLE}</div>
            <div class="days-number">{max(0, delta)}</div>
            <div class="label">days left until {TARGET_DATE.strftime('%B %d, %Y')}</div>
        </div>
    """, unsafe_allow_html=True)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # First, check if the person has logged in
    if check_password():
        # Only if logged in, show the actual timer
        show_timer()
