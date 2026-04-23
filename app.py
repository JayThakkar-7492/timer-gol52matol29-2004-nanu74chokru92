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
    user_input = st.text_input("User ID", key="user_login_unique")
    pass_input = st.text_input("Password", type="password", key="pass_login_unique")
    
    if st.button("Login"):
        if user_input == VALID_USER and pass_input == VALID_PASS:
            st.session_state["authenticated"] = True
            st.rerun() 
        else:
            st.error("Invalid User ID or Password")
    
    return False

def show_timer():
    """The interface of your countdown timer."""
    # Page setup
    st.set_page_config(page_title="Countdown", layout="centered")
    
    # Custom CSS for the UI (same as before)
    st.markdown("""
        <style>
        .timer-card {
            background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
            padding: 40px;
            border-radius: 25px;
            color: #4a4a4a;
            text-align: center;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.1);
            position: relative; /* Keep it above the canvas */
            z-index: 2;
        }
        .title { font-size: 28px; font-weight: bold; margin-bottom: 20px; }
        .days-number { font-size: 90px; font-weight: 800; color: #ff5e62; }
        .label { font-size: 20px; }
        
        /* Ensure canvas covers the background */
        canvas#fireworks_canvas {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
            pointer-events: none; /* Let clicks pass through to the UI */
        }
        </style>
    """, unsafe_allow_html=True)

    # DYNAMIC TIMEZONE LOGIC: Fetches 'today' specifically for India
    today = pd.Timestamp.now(tz='Asia/Kolkata').date()
    delta = (TARGET_DATE - today).days

    # The HTML for the colorful card
    st.markdown(f"""
        <div class="timer-card">
            <div class="title">{TITLE}</div>
            <div class="days-number">{max(0, delta)}</div>
            <div class="label">days left until {TARGET_DATE.strftime('%B %d, %Y')}</div>
        </div>
    """, unsafe_allow_html=True)

    # --- JAVASCRIPT ANIMATION BLOCK ---
    # We inject a simple canvas-based firework particle system.
    st.markdown("""
        <canvas id="fireworks_canvas"></canvas>
        <script>
            const canvas = document.getElementById('fireworks_canvas');
            const ctx = canvas.getContext('2d');
            
            // Set canvas to full screen
            function resize() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }
            window.addEventListener('resize', resize);
            resize();

            class Particle {
                constructor(x, y, color) {
                    this.x = x;
                    this.y = y;
                    this.color = color;
                    this.angle = Math.random() * Math.PI * 2;
                    this.speed = Math.random() * 5 + 2;
                    this.friction = 0.95;
                    this.gravity = 0.05;
                    this.size = Math.random() * 3 + 1;
                    this.alpha = 1;
                    this.decay = Math.random() * 0.01 + 0.005;
                }

                update() {
                    this.speed *= this.friction;
                    this.x += Math.cos(this.angle) * this.speed;
                    this.y += Math.sin(this.angle) * this.speed + this.gravity;
                    this.alpha -= this.decay;
                }

                draw() {
                    ctx.save();
                    ctx.globalAlpha = this.alpha;
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.fillStyle = this.color;
                    ctx.fill();
                    ctx.restore();
                }
            }

            let particles = [];
            const colors = ['#FFD700', '#FF1493', '#00BFFF', '#ADFF2F', '#FF4500'];

            function createFirework() {
                const x = Math.random() * canvas.width;
                const y = Math.random() * canvas.height * 0.7; // Keep them visible
                const color = colors[Math.floor(Math.random() * colors.length)];
                for (let i = 0; i < 50; i++) {
                    particles.push(new Particle(x, y, color));
                }
            }

            function animate() {
                ctx.fillStyle = 'rgba(255, 255, 255, 0.2)'; // Clear background slightly for trail effect
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                
                particles = particles.filter(p => p.alpha > 0);
                particles.forEach(p => {
                    p.update();
                    p.draw();
                });

                requestAnimationFrame(animate);
            }

            animate();
            
            // Burst crackers every 2 seconds
            setInterval(createFirework, 2000);
            
            // Immediate burst on load
            createFirework();
        </script>
    """, unsafe_allow_html=True)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # First, check if the person has logged in
    if check_password():
        # Only if logged in, show the actual timer
        show_timer()
