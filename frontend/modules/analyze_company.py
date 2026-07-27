import streamlit as st
from database import get_all_leads
from company_analysis import analyze_company

def show():
    st.subheader("Analyze Company")

    leads = get_all_leads()

    if not leads:
        st.info("No leads available. Please add a lead first.")
        return

    lead_options = {f"{l[1]} ({l[3]})": l for l in leads}
    selected = st.selectbox("Select a lead to analyze", list(lead_options.keys()))

    if st.button("Run Analysis"):
        lead = lead_options[selected]
        result = analyze_company(lead[1], lead[2])

        st.markdown("### Lead Intelligence")
        st.metric("Qualification Score", f"{result['qualification_score']} / 100")
        st.write(f"**Industry:** {result['industry']}")
        st.write(f"**Insight:** {result['insight']}")
        st.write(f"**Opportunity:** {result['opportunity']}")