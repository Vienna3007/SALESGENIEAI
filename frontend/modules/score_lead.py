import streamlit as st
from database import get_all_leads
from company_analysis import analyze_company

def show():
    st.subheader("Score Lead")

    leads = get_all_leads()
    if not leads:
        st.info("No leads available. Please add a lead first.")
        return

    lead_options = {f"{l[1]} ({l[3]})": l for l in leads}
    selected = st.selectbox("Select a lead to score", list(lead_options.keys()))

    if st.button("Calculate Score"):
        lead = lead_options[selected]
        result = analyze_company(lead[1], lead[2])

        score = result["qualification_score"]
        conversion_probability = min(score + 5, 99)

        st.metric("Lead Score", f"{score} / 100")
        st.progress(conversion_probability / 100)
        st.write(f"**Conversion Probability:** {conversion_probability}%")

        if score >= 80:
            st.success("Priority: High — Highly Qualified Lead")
        elif score >= 60:
            st.warning("Priority: Medium — Needs Nurturing")
        else:
            st.error("Priority: Low — Requires Further Qualification")