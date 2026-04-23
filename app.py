import streamlit as st
from datetime import date

# --- CONFIGURATION ---
TARGET_DATE = date(2026, 5, 1)
TITLE = "Milte hain bahut jaldi!🫶"
VALID_USER = "Nanugolu"
VALID_PASS = "2201200403092004"

def check_password():
    """Returns True if the user had the correct password."""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if st.session_state["authenticated"]:
        return True

    # Login UI
    st.title("🔒 Private Access")
    user_input = st.text_input("User ID")
    pass_input = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if user_input == VALID_USER and pass_input == VALID_PASS:
            st.session_state["authenticated"] = True
            st.rerun() # Refresh to show the timer
        else:
            st.error("Invalid User ID or Password")
    
    return False

def show_timer():
    # This is your existing timer code exactly as it was
    st.set_page_config(page_title="Countdown", layout="centered")
    
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

    today = date.today()
    delta = (TARGET_DATE - today).days

    st.markdown(f"""
        <div class="timer-card">
            <div class="title">{TITLE}</div>
            <div class="days-number">{max(0, delta)}</div>
            <div class="label">days left until {TARGET_DATE.strftime('%B %d, %Y')}</div>
        </div>
    """, unsafe_allow_html=True)

# --- MAIN LOGIC ---
if check_password():
    show_timer()
