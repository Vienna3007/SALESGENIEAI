import streamlit as st

def load_css():
    st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Inter', 'Segoe UI', sans-serif;
    }
    .stApp {
        background-color: #f7f3ee;
    }
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }

    /* ---------- Sidebar brand block (avatar + name) ---------- */
    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        background: #ffffff;
        border: 1px solid #ece3d8;
        border-radius: 14px;
        padding: 14px 16px;
        margin-bottom: 16px !important;
        box-shadow: 0 1px 3px rgba(92, 58, 33, 0.05);
    }
    .sidebar-brand-avatar {
        width: 38px;
        height: 38px;
        min-width: 38px;
        border-radius: 50%;
        background: linear-gradient(135deg, #b5651d, #8a4b1f);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        font-size: 15px;
    }
    .sidebar-brand-text .name {
        font-size: 15.5px;
        font-weight: 700;
        color: #3d2817;
        line-height: 1.2;
    }
    .sidebar-brand-text .subtitle {
        font-size: 11.5px;
        color: #a3927e;
        line-height: 1.2;
    }

    /* ---------- Sidebar section label ---------- */
    .sidebar-section-label {
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #b3a596;
        margin: 4px 0 8px 4px;
    }

    /* ---------- Sidebar nav list (BrewMaster-style) ---------- */
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlockBorderWrapper"],
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] {
        gap: 0.25rem !important;
    }
    section[data-testid="stSidebar"] div[data-testid="element-container"],
    section[data-testid="stSidebar"] div[data-testid="stElementContainer"] {
        margin-bottom: 4px !important;
        margin-top: 0 !important;
    }
    section[data-testid="stSidebar"] .stButton {
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Base style for ALL sidebar nav buttons (inactive = secondary) */
    section[data-testid="stSidebar"] .stButton > button {
        width: 100%;
        display: flex !important;
        justify-content: flex-start !important;
        text-align: left !important;
        background: transparent !important;
        border: none !important;
        border-radius: 10px;
        padding: 10px 14px !important;
        font-weight: 600;
        font-size: 14px;
        color: #6b5745 !important;
        box-shadow: none !important;
    }
    section[data-testid="stSidebar"] .stButton > button:hover {
        background: #f4ead9 !important;
        color: #8a4b1f !important;
        transform: none;
    }
    section[data-testid="stSidebar"] .stButton > button p,
    section[data-testid="stSidebar"] .stButton > button div {
        width: 100%;
        text-align: left !important;
        justify-content: flex-start !important;
        margin: 0 !important;
    }

    /* Active nav item = Streamlit's "primary" button type */
    section[data-testid="stSidebar"] .stButton > button[kind="primary"] {
        background: #b5651d !important;
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover {
        background: #9c5518 !important;
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] .stButton > button[kind="primary"] p {
        color: #ffffff !important;
    }

    /* ---------- Header banner ---------- */
    .app-header {
        background: #ffffff;
        padding: 22px 30px;
        border-radius: 14px;
        margin-bottom: 26px;
        border: 1px solid #ece3d8;
        box-shadow: 0 2px 8px rgba(92, 58, 33, 0.06);
    }
    .app-header h1 {
        color: #4a2e1a;
        margin: 0;
        font-size: 24px;
        font-weight: 700;
        letter-spacing: -0.01em;
    }
    .app-header p {
        color: #8a7563;
        margin: 4px 0 0 0;
        font-size: 13.5px;
        font-weight: 400;
    }

    /* ---------- Stat cards ---------- */
    .stat-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 18px 20px;
        box-shadow: 0 1px 3px rgba(92, 58, 33, 0.06);
        border: 1px solid #ece3d8;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .stat-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 18px rgba(92, 58, 33, 0.10);
    }
    .stat-label {
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 6px;
        color: #a3927e;
    }
    .stat-value {
        color: #3d2817;
        font-size: 28px;
        font-weight: 700;
    }
    .stat-card.c1 .stat-value { color: #b5651d; }
    .stat-card.c2 .stat-value { color: #c0392b; }
    .stat-card.c3 .stat-value { color: #b7791f; }
    .stat-card.c4 .stat-value { color: #2f6f4f; }
    .stat-card.c5 .stat-value { color: #5c3a21; }

    /* ---------- Lead cards ---------- */
    .lead-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 14px 18px;
        margin-bottom: 10px;
        border: 1px solid #ece3d8;
        border-left: 4px solid #b5651d;
        box-shadow: 0 1px 2px rgba(92, 58, 33, 0.05);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .lead-card:hover {
        transform: translateX(3px);
        box-shadow: 0 4px 12px rgba(92, 58, 33, 0.08);
    }
    .lead-company {
        font-size: 15.5px;
        font-weight: 700;
        color: #3d2817;
    }
    .lead-meta {
        font-size: 13px;
        color: #8a7563;
        margin-top: 3px;
    }

    /* ---------- Badges ---------- */
    .badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.02em;
    }
    .badge-hot { background: #fbe1dc; color: #c0392b; }
    .badge-warm { background: #faf0d7; color: #b7791f; }
    .badge-new { background: #f1e6da; color: #b5651d; }
    .badge-cold { background: #e3ede8; color: #2f6f4f; }

    /* ---------- Buttons (main content area) ---------- */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        border: 1px solid #e0c9ac !important;
        background: #ffffff;
        color: #8a4b1f;
        transition: all 0.15s ease;
    }
    .stButton > button:hover {
        background: #b5651d;
        color: white;
        border-color: #b5651d !important;
        transform: translateY(-1px);
        box-shadow: 0 4px 10px rgba(181, 101, 29, 0.25);
    }
    div[data-testid="stFormSubmitButton"] button {
        background: #b5651d !important;
        color: white !important;
        border: none !important;
    }
    div[data-testid="stFormSubmitButton"] button:hover {
        background: #8a4b1f !important;
        box-shadow: 0 4px 10px rgba(181, 101, 29, 0.3);
    }

    /* ---------- Inputs ---------- */
    .stTextInput input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"] > div,
    div[data-baseweb="input"],
    div[data-baseweb="base-input"],
    div[data-baseweb="textarea"] {
        background-color: #ffffff !important;
        color: #3d2817 !important;
        border: 1.5px solid #e8ddd0 !important;
        border-radius: 8px !important;
    }
    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border-color: #b5651d !important;
        box-shadow: 0 0 0 2px rgba(181, 101, 29, 0.12) !important;
    }

    /* ---------- Headings & body text ---------- */
    .stApp, .stApp p, .stApp label, .stApp span {
        color: #3d2817;
    }
    h1, h2, h3, h4, h5 {
        color: #4a2e1a !important;
        font-weight: 700 !important;
    }

    /* ---------- Sidebar container ---------- */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #ece3d8;
        padding-top: 10px;
    }
    section[data-testid="stSidebar"] * {
        color: #5c3a21;
    }

    /* ---------- Alert / Confirmation banners ---------- */
    .duplicate-alert {
        background: #fdf1e0;
        border-left: 5px solid #d68910;
        padding: 14px 18px;
        border-radius: 10px;
        margin-bottom: 15px;
        animation: shake 0.4s ease-in-out;
    }
    .duplicate-alert h4 {
        margin: 0 0 8px 0;
        color: #8a5a00;
    }
    .duplicate-alert p {
        margin: 2px 0;
        color: #5c3a00;
    }
    @keyframes shake {
        0% { transform: translateX(0); }
        25% { transform: translateX(-6px); }
        50% { transform: translateX(6px); }
        75% { transform: translateX(-4px); }
        100% { transform: translateX(0); }
    }
    </style>
    """, unsafe_allow_html=True)