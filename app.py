import streamlit as st
from datetime import date

# --- CONFIGURATION ---
# Target date is fixed here
TARGET_DATE = date(2026, 5, 1) 
TITLE = "Milte hain bahut jaldi!🫶"
# ---------------------

def main():
    st.set_page_config(page_title="Countdown", layout="centered")
    
    # Custom CSS for a beautiful look
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

if __name__ == "__main__":
    main()
