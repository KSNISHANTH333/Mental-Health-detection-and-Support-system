import streamlit as st

st.set_page_config(layout="wide")

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

/* Page background */
.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
}

/* Remove top padding */
.block-container {
    padding-top: 0.5rem;
}

/* -------------------- NAVBAR -------------------- */
.navbar {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: rgba(2, 6, 23, 0.55);
    backdrop-filter: blur(12px);
    padding: 14px 32px;
    border-bottom: 1px solid rgba(255,255,255,0.08);
}

.nav-logo {
    font-size: 28px;
    font-weight: 700;
    color: #22c55e;
}

/* INLINE NAV BUTTONS */
.navbar button {
    background: transparent !important;
    border: none !important;
    padding: 4px 6px !important;   /* VERY SMALL GAP */
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
</style>
""", unsafe_allow_html=True)

# -------------------- AUTH CHECK --------------------
if "logged_in" not in st.session_state:
    st.switch_page("app.py")

# -------------------- NAVBAR --------------------
st.markdown("<div class='navbar'>", unsafe_allow_html=True)

nav_l, nav_c, nav_r = st.columns([3,2,1])

with nav_l:
    st.markdown("<div class='nav-logo'>MindCare</div>", unsafe_allow_html=True)

with nav_c:
    c1, c2, c3, c4 = st.columns([1,1,1,1])

    with c1:
        if st.button("Home"):
            st.switch_page("pages/1_Home.py")

    with c2:
        if st.button("Check"):
            st.switch_page("pages/2_Mental_Check.py")

    with c3:
        if st.button("About"):
            st.switch_page("pages/3_About.py")

    with c4:
        if st.button("Logout"):
            st.session_state.clear()
            st.switch_page("app.py")

with nav_r:
    st.empty()

st.markdown("</div>", unsafe_allow_html=True)

# -------------------- HERO SECTION --------------------
st.markdown("""
<h1 style="font-size:42px; font-weight:800; margin-top:40px;">
Welcome to the Mental Health Support App!
</h1>
<hr style="border:1px solid rgba(255,255,255,0.08);">
""", unsafe_allow_html=True)

st.markdown("""
<h2 style="color:#22c55e;">💚 Your Well-Being Matters</h2>
<p style="color:#cbd5f5; max-width:800px;">
This platform helps students and lecturers understand their emotional state and
guides them toward a healthier mind. You're not alone — we're here for you.
</p>
""", unsafe_allow_html=True)

# -------------------- IMAGE --------------------
st.image(
    "https://illustrations.popsy.co/green/meditation.svg",
    use_container_width=True
)

# -------------------- FEATURES --------------------
st.markdown("""
<h3 style="margin-top:40px;">🌿 What You Can Do Here</h3>
<ul style="line-height:2; color:#e5e7eb;">
<li>✔ Check your mental health status</li>
<li>✔ Understand stress and anxiety levels</li>
<li>✔ Get personalized suggestions</li>
<li>✔ Access emotional support resources</li>
<li>✔ Made for Students and Lecturers</li>
</ul>
""", unsafe_allow_html=True)

# -------------------- REMEMBER MESSAGE --------------------
st.markdown("""
<div style="
    background: rgba(34, 197, 94, 0.15);
    padding: 16px 20px;
    border-radius: 10px;
    margin-top: 30px;
    color: #d1fae5;
    font-size: 16px;
">
💡 <b>Remember:</b> Taking care of your mind is a sign of strength — not weakness.
</div>
""", unsafe_allow_html=True)

# -------------------- THREE TEXT BLOCKS --------------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("😊 **Happiness**  \nYour safe place")

with c2:
    st.markdown("🧠 **Mind Care**  \nDaily check")

with c3:
    st.markdown("🌙 **Balance**  \nStay calm")

# -------------------- CTA BUTTON --------------------
st.markdown("<br>", unsafe_allow_html=True)
if st.button("➡️ Check My Mental Health"):
    st.switch_page("pages/2_Mental_Check.py")

st.markdown("""
<p style="text-align:center; margin-top:40px; color:#9ca3af;">
Made with ❤️ for supporting mental well-being.
</p>
""", unsafe_allow_html=True)
