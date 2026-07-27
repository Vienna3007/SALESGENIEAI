import streamlit as st

def load_css():
    st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Inter', 'Segoe UI', sans-serif;
        font-size: 17px;
    }
    .stApp {
        background-color: #f7f3ee;
    }
    header[data-testid="stHeader"] {
        background-color: rgba(0,0,0,0) !important;
    }

    /* ---------- Hide sidebar entirely (unused) ---------- */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    .block-container {
        padding-top: 1.5rem;
        padding-left: 1.5rem;
        padding-right: 1.5rem;
        padding-bottom: 1.5rem;
        max-width: 100%;
    }

    /* ---------- Header banner ---------- */
    .app-header {
        background: #ffffff;
        padding: 20px 26px;
        border-radius: 14px;
        margin-bottom: 22px;
        border: 1px solid #ece3d8;
    }
    .app-header-brand {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    .app-header-avatar {
        width: 44px;
        height: 44px;
        min-width: 44px;
        border-radius: 12px;
        background: #b5651d;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        font-size: 16px;
    }
    .app-header h1 {
        color: #4a2e1a;
        margin: 0;
        font-size: 26px;
        font-weight: 700;
        letter-spacing: -0.01em;
    }
    .app-header p {
        color: #8a7563;
        margin: 2px 0 0 0;
        font-size: 15px;
        font-weight: 400;
    }

    /* ---------- Tab bar ---------- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        border-bottom: 1px solid #ece3d8;
        margin-bottom: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 44px;
        padding: 0 20px;
        background: transparent;
        border-radius: 8px 8px 0 0;
        color: #8a7563;
        font-weight: 600;
        font-size: 16px;
    }
    .stTabs [aria-selected="true"] {
        color: #b5651d !important;
        border-bottom: 2px solid #b5651d !important;
    }

    /* ---------- Stat cards ---------- */
    .stat-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 16px 18px;
        border: 1px solid #ece3d8;
    }
    .stat-label {
        font-size: 13px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-bottom: 6px;
        color: #a3927e;
    }
    .stat-value {
        color: #3d2817;
        font-size: 30px;
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
        border-radius: 10px;
        padding: 12px 16px;
        margin-bottom: 8px;
        border: 1px solid #ece3d8;
        border-left: 3px solid #b5651d;
    }
    .lead-company {
        font-size: 17px;
        font-weight: 700;
        color: #3d2817;
    }
    .lead-meta {
        font-size: 14px;
        color: #8a7563;
        margin-top: 3px;
    }

    /* ---------- Scrollbars ---------- */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-track {
        background: #f1e6da;
        border-radius: 8px;
    }
    ::-webkit-scrollbar-thumb {
        background: #d8ac7a;
        border-radius: 8px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #b5651d;
    }

    /* ---------- Leads master-detail layout ---------- */
    .lead-list-item {
        padding-bottom: 10px;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:has(.lead-list-item-active) {
        border-color: #b5651d !important;
        background: #fdf6ee !important;
    }
    .lead-empty-state {
        background: #ffffff;
        border: 1px dashed #ece3d8;
        border-radius: 12px;
        padding: 40px 20px;
        text-align: center;
        color: #a3927e;
        font-size: 15px;
    }
    .detail-header {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 14px;
    }
    .detail-header h3 {
        margin: 0;
    }

    /* ---------- Badges ---------- */
    .badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.02em;
        margin-left: 6px;
    }
    .badge-hot { background: #fbe1dc; color: #c0392b; }
    .badge-warm { background: #faf0d7; color: #b7791f; }
    .badge-new { background: #f1e6da; color: #b5651d; }
    .badge-cold { background: #e3ede8; color: #2f6f4f; }

    /* ---------- Buttons ---------- */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        border: 1px solid #e0c9ac !important;
        background: #ffffff;
        color: #8a4b1f;
        transition: all 0.12s ease;
    }
    .stButton > button:hover {
        background: #b5651d;
        color: white;
        border-color: #b5651d !important;
    }
    div[data-testid="stFormSubmitButton"] button {
        background: #b5651d !important;
        border: none !important;
    }
    div[data-testid="stFormSubmitButton"] button p {
        color: #ffffff !important;
        font-weight: 700 !important;
    }
    div[data-testid="stFormSubmitButton"] button:hover {
        background: #8a4b1f !important;
    }
    .stButton > button:disabled {
        background: #f1e6da !important;
        border-color: #ece3d8 !important;
        opacity: 1 !important;
    }
    .stButton > button:disabled p {
        color: #b5651d !important;
        font-weight: 700 !important;
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
        border: 1px solid #e8ddd0 !important;
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

    /* ---------- Alert / Confirmation banners ---------- */
    .duplicate-alert {
        background: #fdf1e0;
        border-left: 5px solid #d68910;
        padding: 14px 18px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .duplicate-alert h4 {
        margin: 0 0 8px 0;
        color: #8a5a00;
    }
    .duplicate-alert p {
        margin: 2px 0;
        color: #5c3a00;
    }
    </style>
    """, unsafe_allow_html=True)