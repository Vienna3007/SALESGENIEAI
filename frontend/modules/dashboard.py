import streamlit as st
from database import get_all_leads, delete_lead, get_lead_by_id

def show():
    st.subheader("Sales Dashboard")

    leads = get_all_leads()
    total_leads = len(leads)
    hot_leads = sum(1 for l in leads if l[6] == "Hot")
    warm_leads = sum(1 for l in leads if l[6] == "Warm")
    emails_sent = 0
    calls_done = 0

    stats = [
        ("Total Leads", total_leads, "c1"),
        ("Hot Leads", hot_leads, "c2"),
        ("Warm Leads", warm_leads, "c3"),
        ("Emails Sent", emails_sent, "c4"),
        ("Calls Done", calls_done, "c5"),
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

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("All Leads")

    if "confirm_delete_id" not in st.session_state:
        st.session_state.confirm_delete_id = None

    # ---- Confirmation prompt shown above the list if a delete was requested ----
    if st.session_state.confirm_delete_id is not None:
        lead_to_delete = get_lead_by_id(st.session_state.confirm_delete_id)
        if lead_to_delete:
            st.markdown(f"""
                <div class="duplicate-alert">
                    <h4>🗑️ Confirm Deletion</h4>
                    <p>Are you sure you want to permanently delete
                    <b>{lead_to_delete[1]}</b> ({lead_to_delete[3]} | {lead_to_delete[4]})?</p>
                    <p>This action cannot be undone.</p>
                </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Yes, Delete", use_container_width=True, key="confirm_delete_yes"):
                    delete_lead(st.session_state.confirm_delete_id)
                    st.success(f"Lead '{lead_to_delete[1]}' deleted successfully!")
                    st.session_state.confirm_delete_id = None
                    st.rerun()
            with col2:
                if st.button("❌ No, Keep It", use_container_width=True, key="confirm_delete_no"):
                    st.info("Deletion cancelled.")
                    st.session_state.confirm_delete_id = None
                    st.rerun()
        else:
            st.session_state.confirm_delete_id = None

    # ---- Lead list ----
    if leads:
        badge_map = {
            "Hot": "badge-hot",
            "Warm": "badge-warm",
            "New": "badge-new",
            "Cold": "badge-cold",
        }
        for lead in leads:
            lead_id = lead[0]
            status = lead[6] or "New"
            badge_class = badge_map.get(status, "badge-new")

            card_col, btn_col = st.columns([6, 1])
            with card_col:
                st.markdown(f"""
                    <div class="lead-card">
                        <div class="lead-company">{lead[1]} <span class="badge {badge_class}">{status}</span></div>
                        <div class="lead-meta">{lead[3]} &nbsp;|&nbsp; {lead[4]} &nbsp;|&nbsp; {lead[5]} &nbsp;|&nbsp; {lead[2]}</div>
                    </div>
                """, unsafe_allow_html=True)
            with btn_col:
                if st.button("🗑️ Delete", key=f"delete_{lead_id}"):
                    st.session_state.confirm_delete_id = lead_id
                    st.rerun()
    else:
        st.info("No leads added yet. Go to 'Add Lead' to create one.")