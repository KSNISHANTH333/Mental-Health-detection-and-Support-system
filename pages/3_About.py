import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

# -------------------- GLOBAL STYLES (SAME AS HOME & CHECK) --------------------
st.markdown("""
<style>

/* Hide sidebar */
[data-testid="stSidebar"],
[data-testid="stSidebarNav"] {
    display: none;
}

/* Transparent header */
header[data-testid="stHeader"] {
    background: transparent;
    box-shadow: none;
}

/* Page background */
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
}

/* Reduce top padding */
.block-container {
    padding-top: 0.8rem;
}

/* Navbar */
.navbar {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: rgba(2, 6, 23, 0.55);
    backdrop-filter: blur(12px);
    padding: 14px 40px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

.nav-logo {
    font-size: 26px;
    font-weight: 700;
    color: #22c55e;
}

/* Navbar buttons */
.navbar button {
    background: transparent !important;
    border: none !important;
    padding: 4px 6px !important;
    margin: 0 6px !important;
    box-shadow: none !important;
}

.navbar button span {
    font-size: 16px;
    font-weight: 500;
    color: #e5e7eb;
}

.navbar button:hover span {
    color: #22c55e;
}

/* ---------- YOUR EXISTING CONTENT STYLES (UNCHANGED) ---------- */
.main-title {
    font-size: 42px;
    font-weight: 700;
    margin-top: 30px;
}

.divider {
    border-top: 1px solid rgba(255,255,255,0.12);
    margin: 30px 0;
}

.section {
    margin-top: 30px;
}

.footer-text {
    color: #22c55e;
    font-size: 26px;
    font-weight: 600;
    text-align: center;
    margin-top: 40px;
}

.team-card {
    background-color: #f5f5f5;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    max-width: 520px;
    margin: 30px auto;
}

.team-card h2 {
    margin-bottom: 12px;
    font-size: 22px;
    color: #111111;
}

.team-card p {
    font-size: 14px;
    color: #222;
    margin: 6px 0;
    line-height: 1.5;
}

.team-card a {
    color: #0066cc;
    text-decoration: none;
}
</style>
""", unsafe_allow_html=True)

# -------------------- AUTH CHECK --------------------
if "logged_in" not in st.session_state:
    st.switch_page("app.py")

# -------------------- NAVBAR (SAME AS OTHER PAGES) --------------------
st.markdown("<div class='navbar'>", unsafe_allow_html=True)

l, c, r = st.columns([3,2,1])

with l:
    st.markdown("<div class='nav-logo'>MindCare</div>", unsafe_allow_html=True)

with c:
    n1, n2, n3, n4 = st.columns(4)

    with n1:
        if st.button("Home"):
            st.switch_page("pages/1_Home.py")

    with n2:
        if st.button("Check"):
            st.switch_page("pages/2_Mental_Check.py")

    with n3:
        if st.button("About"):
            st.switch_page("pages/3_About.py")

    with n4:
        if st.button("Logout"):
            st.session_state.clear()
            st.switch_page("app.py")

with r:
    st.empty()

st.markdown("</div>", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.markdown("<div class='main-title'>ℹ️ About This Page</div>", unsafe_allow_html=True)
st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# -------------------- DESCRIPTION --------------------
st.markdown("""
This <b>Mental Health Support App</b> is designed to help students and lecturers
assess their mental health and emotional well-being.
<br><br>
It provides role-specific questionnaires and actionable insights, promoting awareness about
stress, anxiety, and healthy coping strategies.
""", unsafe_allow_html=True)

# -------------------- PURPOSE --------------------
st.markdown("""
<div class="section">
<h3>🎯 Purpose of the App</h3>
<ul>
    <li>Assess mental health in a simple and private manner</li>
    <li>Provide role-specific questionnaires</li>
    <li>Increase awareness of stress and anxiety</li>
    <li>Support emotional well-being</li>
</ul>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# -------------------- IMAGE --------------------
BASE_DIR = Path(__file__).resolve().parent.parent
ABOUT_IMG = BASE_DIR / "assets" / "about.jpg"

col1, col2, col3 = st.columns([3, 2, 3])

with col2:
    st.image(str(ABOUT_IMG), width=220)

# -------------------- FOOTER QUOTE --------------------
st.markdown("""
<div class="footer-text">
💚 Take care of your mind — it's your greatest asset!
</div>
""", unsafe_allow_html=True)

# -------------------- PROJECT TEAM --------------------
st.markdown("""
<div class="team-card">
  <h2>🧑‍💻 Project Team</h2>

  <p><b>KS Nishanth</b><br>
  Developer & Designer</p>

  <p><b>Uday Kumar</b><br>
  Researcher & Tester</p>

  <p>
    📧 <a href="mailto:checkhealth@gmail.com">checkhealth@gmail.com</a><br>
    📞 8636363636
  </p>

  <p style="font-size:13px; color:#555;">
    Made with ❤️ for supporting mental well-being.
  </p>
</div>
""", unsafe_allow_html=True)
