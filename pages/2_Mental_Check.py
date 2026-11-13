import streamlit as st

st.set_page_config(layout="wide")

# -------------------- GLOBAL STYLES (SAME AS HOME) --------------------
st.markdown("""
<style>
[data-testid="stSidebar"],
[data-testid="stSidebarNav"] { display: none; }

header[data-testid="stHeader"] {
    background: transparent;
    box-shadow: none;
}

.stApp {
    background: radial-gradient(circle at top, #0f172a, #020617);
    color: white;
}

.block-container { padding-top: 0.8rem; }

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
</style>
""", unsafe_allow_html=True)

# -------------------- AUTH CHECK --------------------
if "logged_in" not in st.session_state:
    st.switch_page("app.py")

# -------------------- NAVBAR --------------------
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

# -------------------- PAGE CONTENT --------------------
st.markdown("""
<h1 style="font-size:38px; font-weight:800;">🧠 Mental Health Check</h1>
<p style="color:#9ca3af;">
This is your health assessment page. This is <b>not</b> a medical diagnosis.
</p>
<hr style="border:1px solid rgba(255,255,255,0.08);">
""", unsafe_allow_html=True)

# -------------------- ROLE & INFO --------------------
role = st.selectbox("Who are you?", ["Student", "Lecturer", "Other"])
gender = st.selectbox("Gender", ["-", "Male", "Female", "Other"])
age_group = st.selectbox("Age group", ["-", "Below 18", "18–24", "25–34", "35+"])

options = ["Prefer not to say", "Never", "Sometimes", "Often", "Always"]

q1 = st.selectbox("How stressed do you feel due to studies?", options)
q2 = st.selectbox("How often do you feel pressure due to exams or assignments?", options)
q3 = st.selectbox("Do you feel motivated to attend classes?", options)
q4 = st.selectbox("How often do you feel anxious?", options)
q5 = st.selectbox("How well are you sleeping recently?", options)
q6 = st.selectbox("How often do you feel difficulty concentrating?", options)
q7 = st.selectbox("Do you feel supported by friends or teachers?", options)

suicide_q = st.selectbox(
    "Have you had thoughts about harming yourself or feeling that life is not worth living?",
    ["No", "Sometimes", "Often", "Prefer not to say"]
)

# -------------------- SUBMIT --------------------
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Submit Assessment"):

    mental_answers = [q1, q2, q3, q4, q5, q6, q7]

    if all(ans == "Prefer not to say" for ans in mental_answers):
        st.warning("⚠️ Please answer at least one question so we can understand your state better.")

    else:
        # Gender-based tone
        if gender == "Male":
            tone = "You may be carrying a lot internally, even if you don’t always express it."
        elif gender == "Female":
            tone = "You might be managing many expectations, both emotionally and mentally."
        else:
            tone = "Everyone experiences mental pressure differently, and your feelings are valid."

        # Suicide risk (ONLY RED)
        if suicide_q in ["Sometimes", "Often"]:
            st.error(
                f"🔴 This response suggests emotional risk.\n\n"
                f"{tone} You are not alone, and help is available. "
                "Please reach out to a trusted person or a mental health professional immediately."
            )

        else:
            high = mental_answers.count("Often") + mental_answers.count("Always")
            mid = mental_answers.count("Sometimes")

            # HIGH STRESS (ORANGE)
            if high >= 4:
                st.warning(
                    f"🟠 High stress detected.\n\n"
                    f"{tone} Your answers suggest significant academic or emotional pressure. "
                    "Taking breaks, improving sleep, and talking to someone you trust could help."
                )

            # MODERATE (BLUE)
            elif mid >= 3:
                st.info(
                    f"🔵 Moderate stress level.\n\n"
                    f"{tone} You seem to be managing, but some areas like focus or rest may need attention."
                )

            # POSITIVE / HEALTHY (GREEN)
            else:
                st.success(
                    f"🟢 Positive mental well-being.\n\n"
                    f"{tone} You appear to be coping well and maintaining balance. "
                    "Continue your healthy habits and support system."
                )

st.markdown("""
<p style="text-align:center; margin-top:40px; color:#9ca3af;">
Your well-being matters.
</p>
""", unsafe_allow_html=True)
