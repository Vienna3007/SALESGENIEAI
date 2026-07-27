import streamlit as st
from database import init_db
<<<<<<< HEAD
from modules import tabs_view
from styles import load_css

st.set_page_config(
    page_title="SalesGenie AI",
    layout="wide",
    initial_sidebar_state="collapsed",
)
=======
from modules import dashboard, add_lead, analyze_company, generate_email, score_lead, summarize_call
from styles import load_css

st.set_page_config(page_title="SalesGenie AI", layout="wide")
>>>>>>> b4c743a0ab5aa6935c3e4719b56ed7dbef30884a

init_db()
load_css()

<<<<<<< HEAD
st.markdown("""
    <div class="app-header">
        <div class="app-header-brand">
            <div class="app-header-avatar">SG</div>
            <div>
                <h1>SalesGenie AI</h1>
                <p>AI powered sales assistant and lead intelligence platform</p>
            </div>
=======
if "active_module" not in st.session_state:
    st.session_state.active_module = "Dashboard"

st.sidebar.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-brand-avatar">SG</div>
        <div class="sidebar-brand-text">
            <div class="name">SalesGenie AI</div>
            <div class="subtitle">Admin Dashboard</div>
>>>>>>> b4c743a0ab5aa6935c3e4719b56ed7dbef30884a
        </div>
    </div>
""", unsafe_allow_html=True)

<<<<<<< HEAD
tabs_view.show()
=======
nav_items = [
    ("Dashboard", "▦  Dashboard"),
    ("Add Lead", "＋  Add Lead"),
    ("Analyze Company", "⌕  Analyze Company"),
    ("Generate Email", "✉  Generate Email"),
    ("Score Lead", "★  Score Lead"),
    ("Summarize Call", "☎  Summarize Call"),
]

for key, label in nav_items:
    is_active = st.session_state.active_module == key
    if st.sidebar.button(
        label,
        key=f"nav_{key}",
        use_container_width=True,
        type="primary" if is_active else "secondary"
    ):
        st.session_state.active_module = key
        st.rerun()

module = st.session_state.active_module

st.markdown("""
    <div class="app-header">
        <h1>SalesGenie AI</h1>
        <p>AI Powered Sales Assistant & Lead Intelligence Platform</p>
    </div>
""", unsafe_allow_html=True)

if module == "Add Lead":
    add_lead.show()
elif module == "Analyze Company":
    analyze_company.show()
elif module == "Generate Email":
    generate_email.show()
elif module == "Score Lead":
    score_lead.show()
elif module == "Summarize Call":
    summarize_call.show()
elif module == "Dashboard":
    dashboard.show()
>>>>>>> b4c743a0ab5aa6935c3e4719b56ed7dbef30884a
