import streamlit as st
from database import init_db
from modules import tabs_view
from styles import load_css

st.set_page_config(
    page_title="SalesGenie AI",
    layout="wide",
    initial_sidebar_state="collapsed",
)

init_db()
load_css()

st.markdown("""
    <div class="app-header">
        <div class="app-header-brand">
            <div class="app-header-avatar">SG</div>
            <div>
                <h1>SalesGenie AI</h1>
                <p>AI powered sales assistant and lead intelligence platform</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

tabs_view.show()