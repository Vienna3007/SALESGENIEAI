import streamlit as st
from database import get_all_leads

def show():
    st.subheader("Generate Email")

    leads = get_all_leads()
    if not leads:
        st.info("No leads available. Please add a lead first.")
        return

    lead_options = {f"{l[1]} ({l[3]})": l for l in leads}
    selected = st.selectbox("Select a lead", list(lead_options.keys()))

    if st.button("Generate Outreach Email"):
        lead = lead_options[selected]
        company, industry, contact = lead[1], lead[2], lead[3]

        subject = f"Helping {company} streamline operations with AI"
        body = f"""Hi {contact},

I noticed {company} operates in the {industry} space, and wanted to reach out.

We've helped similar companies improve efficiency and reduce manual overhead
using AI-driven automation. I'd love to share how this could apply to {company}
specifically.

Would you be open to a quick 15-minute call this week?

Best regards,
Sales Team
"""
        st.text_input("Subject", value=subject)
        st.text_area("Email Body", value=body, height=250)