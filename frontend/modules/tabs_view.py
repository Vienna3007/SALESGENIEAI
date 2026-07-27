import streamlit as st
from database import get_all_leads
from modules import leads_tab, generate_email, score_lead, summarize_call, analyze_company


def render_outreach_tab():
    st.subheader("Outreach")
    col_email, col_score = st.columns(2)

    with col_email:
        st.markdown("#### AI email generator")
        generate_email.show()

    with col_score:
        st.markdown("#### Lead score")
        score_lead.show()


def render_conversations_tab():
    st.subheader("Conversations")
    col_summary, col_intel = st.columns(2)

    with col_summary:
        st.markdown("#### Call summary")
        summarize_call.show()

    with col_intel:
        st.markdown("#### Company intelligence")
        analyze_company.show()


def render_dashboard_tab():
    st.subheader("Dashboard")
    leads = get_all_leads() + leads_tab._build_sample_leads()
    total_leads = len(leads)
    hot_leads = sum(1 for l in leads if l[6] == "Hot")
    warm_leads = sum(1 for l in leads if l[6] == "Warm")
    new_leads = sum(1 for l in leads if (l[6] or "New") == "New")
    cold_leads = sum(1 for l in leads if l[6] == "Cold")

    stats = [
        ("Total leads", total_leads, "c1"),
        ("Hot leads", hot_leads, "c2"),
        ("Warm leads", warm_leads, "c3"),
        ("New leads", new_leads, "c4"),
        ("Cold leads", cold_leads, "c5"),
    ]
    cols = st.columns(len(stats))
    for col, (label, value, color_class) in zip(cols, stats):
        with col:
            st.markdown(f"""
                <div class="stat-card {color_class}">
                    <div class="stat-label">{label}</div>
                    <div class="stat-value">{value}</div>
                </div>
            """, unsafe_allow_html=True)

    


def show():
    tab1, tab2, tab3, tab4 = st.tabs(["Leads", "Outreach", "Conversations", "Dashboard"])
    with tab1:
        leads_tab.show()
    with tab2:
        render_outreach_tab()
    with tab3:
        render_conversations_tab()
    with tab4:
        render_dashboard_tab()