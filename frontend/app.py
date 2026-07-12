import streamlit as st
from database import init_db
from modules import dashboard, add_lead, analyze_company, generate_email, score_lead, summarize_call
from styles import load_css

st.set_page_config(page_title="SalesGenie AI", layout="wide")

init_db()
load_css()

if "active_module" not in st.session_state:
    st.session_state.active_module = "Dashboard"

st.sidebar.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-brand-avatar">SG</div>
        <div class="sidebar-brand-text">
            <div class="name">SalesGenie AI</div>
            <div class="subtitle">Admin Dashboard</div>
        </div>
    </div>
""", unsafe_allow_html=True)

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