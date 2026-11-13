import streamlit as st
import json
import hashlib
from pathlib import Path
import base64

st.set_page_config(layout="wide")

# -------------------- PATH --------------------
BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "assets" / "logo.png"

# -------------------- IMAGE TO BASE64 --------------------
def image_to_base64(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

logo_base64 = image_to_base64(LOGO_PATH)

# -------------------- GLOBAL STYLES --------------------
st.markdown("""
<style>

/* Hide Streamlit default UI */
[data-testid="stSidebar"],
[data-testid="stSidebarNav"] {
    display: none;
}

header[data-testid="stHeader"] {
    background: transparent;
    box-shadow: none;
}

/* Background */
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
}

/* Center container */
.login-wrapper {
    max-width: 900px;
    margin: 80px auto;
}

/* Header row (logo + title) */
.header-row {
    display: flex;
    align-items: center;
    gap: 25px;
    margin-bottom: 15px;
}

/* Round logo */
.logo {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    overflow: hidden;
    flex-shrink: 0;
}

/* Title */
.title {
    font-size: 42px;
    font-weight: 800;
    color: #22c55e;
}

/* Subtitle */
.subtitle {
    color: #9ca3af;
    margin-top: 6px;
}

/* Inputs */
input {
    background: #1f2933 !important;
    color: white !important;
}

/* Buttons */
.stButton > button {
    width: auto;
    padding: 10px 22px;
    border-radius: 10px;
    font-weight: 600;
}

/* Login button */
.login-btn button {
    background: transparent;
    border: 1px solid rgba(255,255,255,0.4);
    color: white;
}

/* Create account */
.create-btn button {
    background: transparent;
    border: 1px solid rgba(255,255,255,0.25);
    color: #e5e7eb;
    margin-top: 12px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- USER FUNCTIONS --------------------
def load_users():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_users(users):
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)

def hash_pwd(p):
    return hashlib.sha256(p.encode()).hexdigest()

# -------------------- LOGIN UI --------------------
st.markdown('<div class="login-wrapper">', unsafe_allow_html=True)

# ✅ LOGO + TITLE ROW (MATCHES IMAGE)
st.markdown(f"""
<div class="header-row">
    <div class="logo">
        <img src="data:image/png;base64,{logo_base64}"
             style="width:100%; height:100%; object-fit:cover;">
    </div>
<div>
    <div class="title">Welcome To Mind Care 👋</div>
    <div class="subtitle">
        Login to access your personal mental health dashboard.
    </div>
</div>

</div>
<hr style="border:1px solid rgba(255,255,255,0.15); margin:30px 0;">
""", unsafe_allow_html=True)

username = st.text_input("Username (Email)")
password = st.text_input("Password", type="password")

# -------------------- LOGIN BUTTON --------------------
st.markdown('<div class="login-btn">', unsafe_allow_html=True)
if st.button("Login"):
    for u in load_users():
        if u["username"] == username and u["password"] == hash_pwd(password):
            st.session_state.logged_in = True
            st.switch_page("pages/1_Home.py")
    st.error("Invalid credentials")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------- CREATE ACCOUNT --------------------
st.markdown('<div class="create-btn">', unsafe_allow_html=True)
if st.button("Create New Account"):
    if username and password:
        users = load_users()
        users.append({"username": username, "password": hash_pwd(password)})
        save_users(users)
        st.success("Account created successfully. Please login.")
    else:
        st.warning("Enter username and password")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
