import streamlit as st
from database import get_all_leads, get_lead_by_id, update_lead, update_lead_status, delete_lead, add_lead, find_duplicate_lead

STATUS_OPTIONS = ["New", "Hot", "Warm", "Cold", "Contacted", "Qualified"]
BADGE_MAP = {"Hot": "badge-hot", "Warm": "badge-warm", "New": "badge-new", "Cold": "badge-cold"}

_SAMPLE_COMPANIES = [
    ("Nimbus Tech", "Technology", "Rahul Mehta", "rahul.mehta@nimbustech.io", "9810012345", "New"),
    ("Blue Harbor Inc", "Finance", "Sarah Collins", "sarah.collins@blueharbor.com", "9810023456", "Hot"),
    ("Fenwick Labs", "Healthcare", "Amit Sharma", "amit.sharma@fenwicklabs.com", "9810034567", "Warm"),
    ("Grantline Manufacturing", "Manufacturing", "Priya Nair", "priya.nair@grantline.com", "9810045678", "New"),
    ("Coral Retail Group", "Retail", "David Kim", "david.kim@coralretail.com", "9810056789", "Cold"),
    ("Vertex Financial", "Finance", "Meera Iyer", "meera.iyer@vertexfin.com", "9810067890", "Hot"),
    ("Solstice Health", "Healthcare", "John Abraham", "john.abraham@solsticehealth.com", "9810078901", "Qualified"),
    ("Ironclad Systems", "Technology", "Neha Verma", "neha.verma@ironcladsys.com", "9810089012", "Warm"),
    ("Harborline Retail", "Retail", "Kevin Rose", "kevin.rose@harborline.com", "9810090123", "New"),
    ("Prime Manufacturing Co", "Manufacturing", "Anjali Gupta", "anjali.gupta@primemfg.com", "9810001234", "Contacted"),
    ("Skyline Finance", "Finance", "Ravi Kumar", "ravi.kumar@skylinefin.com", "9810011235", "Hot"),
    ("Cedarwood Health", "Healthcare", "Sophia Turner", "sophia.turner@cedarwoodhealth.com", "9810022346", "New"),
    ("Quantum Retail", "Retail", "Arjun Reddy", "arjun.reddy@quantumretail.com", "9810033457", "Warm"),
    ("Northgate Tech", "Technology", "Emily Davis", "emily.davis@northgatetech.com", "9810044568", "Qualified"),
    ("Bridgeline Manufacturing", "Manufacturing", "Karan Malhotra", "karan.malhotra@bridgeline.com", "9810055679", "Cold"),
    ("Anchor Financial", "Finance", "Isha Kapoor", "isha.kapoor@anchorfin.com", "9810066780", "New"),
    ("Wellspring Health", "Healthcare", "Michael Chen", "michael.chen@wellspringhealth.com", "9810077891", "Hot"),
    ("Retail Nexus", "Retail", "Divya Menon", "divya.menon@retailnexus.com", "9810088902", "Contacted"),
    ("Coreline Technologies", "Technology", "Sam Wilson", "sam.wilson@corelinetech.com", "9810099013", "Warm"),
    ("Summit Manufacturing", "Manufacturing", "Pooja Rao", "pooja.rao@summitmfg.com", "9810000124", "New"),
]


def _build_sample_leads():
    leads = []
    for i, (company, industry, contact, email, phone, status) in enumerate(_SAMPLE_COMPANIES, start=1):
        lead_id = f"sample-{i}"
        leads.append((lead_id, company, industry, contact, email, phone, status, "2026-07-01"))
    return leads


def _is_sample(lead_id):
    return isinstance(lead_id, str) and lead_id.startswith("sample-")


def _get_sample_lead(lead_id):
    for lead in _build_sample_leads():
        if lead[0] == lead_id:
            return lead
    return None


def _badge_class(status):
    return BADGE_MAP.get(status, "badge-new")


def _render_add_lead_form():
    with st.form("add_lead_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            company_name = st.text_input("Company name")
            contact_name = st.text_input("Contact name")
            email = st.text_input("Email")
        with col2:
            industry = st.text_input("Industry")
            phone = st.text_input("Phone")

        submitted = st.form_submit_button("Add lead")

        if submitted:
            fields = {
                "Company name": company_name, "Industry": industry,
                "Contact name": contact_name, "Email": email, "Phone": phone,
            }
            missing = [name for name, val in fields.items() if not val.strip()]
            if missing:
                st.error(f"All fields are required. Missing: {', '.join(missing)}")
            else:
                duplicate = find_duplicate_lead(email, phone)
                if duplicate:
                    st.warning(f"A lead with this email or phone already exists: {duplicate[1]}")
                else:
                    result = add_lead(company_name.strip(), industry.strip(),
                                       contact_name.strip(), email.strip(), phone.strip())
                    st.session_state.selected_lead_id = result.get("id", result.get("lead_id"))
                    st.session_state.show_add_form = False
                    st.rerun()


def _render_search_list(leads):
    with st.container(height=520, border=True):
        search = st.text_input("Search leads", placeholder="Search by company or contact name", label_visibility="collapsed")

        filtered = leads
        if search:
            q = search.lower().strip()
            filtered = [l for l in leads if q in l[1].lower() or q in l[3].lower()]

        total_matches = len(filtered)
        filtered = filtered[:20]

        count_label = f"{total_matches} lead{'s' if total_matches != 1 else ''}"
        if total_matches > 20:
            count_label += " (showing first 20 — refine your search)"
        st.markdown(f"<p style='font-size:12.5px; color:var(--text-secondary, #8a7563); margin:6px 0 10px;'>{count_label}</p>", unsafe_allow_html=True)

        if not filtered:
            st.info("No leads match your search.")
            return

        for lead in filtered:
            lead_id, company, industry, contact, email, phone, status, created_at = lead
            is_selected = st.session_state.get("selected_lead_id") == lead_id
            badge_class = _badge_class(status or "New")

            with st.container(border=True):
                info_col, btn_col = st.columns([3, 1], vertical_alignment="center")
                with info_col:
                    st.markdown(f"""
                        <div class="lead-list-item {'lead-list-item-active' if is_selected else ''}">
                            <div class="lead-company">{company}<span class="badge {badge_class}">{status or 'New'}</span></div>
                            <div class="lead-meta">{contact} &nbsp;|&nbsp; {industry}</div>
                        </div>
                    """, unsafe_allow_html=True)
                with btn_col:
                    if st.button("Viewing" if is_selected else "View", key=f"select_{lead_id}",
                                 use_container_width=True, disabled=is_selected):
                        st.session_state.selected_lead_id = lead_id
                        st.rerun()


def _render_detail_panel():
    lead_id = st.session_state.get("selected_lead_id")

    if lead_id is None:
        st.markdown("""
            <div class="lead-empty-state">
                <p>Select a lead from the list to view details</p>
            </div>
        """, unsafe_allow_html=True)
        return

    if _is_sample(lead_id):
        lead = _get_sample_lead(lead_id)
        if lead is None:
            st.session_state.selected_lead_id = None
            return
        _, company, industry, contact, email, phone, status, created_at = lead

        st.markdown(f"""
            <div class="detail-header">
                <h3>{company}</h3>
                <span class="badge {_badge_class(status or 'New')}">{status or 'New'}</span>
            </div>
        """, unsafe_allow_html=True)
        st.caption("Sample lead — for reference only, not stored in your database.")

        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Company name", value=company, disabled=True)
            st.text_input("Contact name", value=contact, disabled=True)
            st.text_input("Email", value=email, disabled=True)
        with col2:
            st.text_input("Industry", value=industry, disabled=True)
            st.text_input("Phone", value=phone, disabled=True)
            st.text_input("Status", value=status, disabled=True)
        return

    lead = get_lead_by_id(lead_id)
    if lead is None:
        st.session_state.selected_lead_id = None
        st.info("That lead no longer exists.")
        return

    lead_id, company, industry, contact, email, phone, status, created_at = lead

    st.markdown(f"""
        <div class="detail-header">
            <h3>{company}</h3>
            <span class="badge {_badge_class(status or 'New')}">{status or 'New'}</span>
        </div>
    """, unsafe_allow_html=True)

    with st.form(f"edit_lead_{lead_id}"):
        col1, col2 = st.columns(2)
        with col1:
            new_company = st.text_input("Company name", value=company)
            new_contact = st.text_input("Contact name", value=contact)
            new_email = st.text_input("Email", value=email)
        with col2:
            new_industry = st.text_input("Industry", value=industry)
            new_phone = st.text_input("Phone", value=phone)
            new_status = st.selectbox("Status", STATUS_OPTIONS,
                                       index=STATUS_OPTIONS.index(status) if status in STATUS_OPTIONS else 0)

        save_col, delete_col = st.columns([3, 1])
        with save_col:
            save_clicked = st.form_submit_button("Save changes", use_container_width=True)
        with delete_col:
            delete_clicked = st.form_submit_button("Delete", use_container_width=True)

        if save_clicked:
            update_lead(lead_id, new_company.strip(), new_industry.strip(),
                        new_contact.strip(), new_email.strip(), new_phone.strip())
            if new_status != status:
                update_lead_status(lead_id, new_status)
            st.success("Lead updated.")
            st.rerun()

        if delete_clicked:
            st.session_state.confirm_delete_id = lead_id
            st.rerun()

    if st.session_state.get("confirm_delete_id") == lead_id:
        st.markdown(f"""
            <div class="duplicate-alert">
                <h4>Confirm deletion</h4>
                <p>Delete <b>{company}</b> permanently? This can't be undone.</p>
            </div>
        """, unsafe_allow_html=True)
        yes_col, no_col = st.columns(2)
        with yes_col:
            if st.button("Yes, delete", key=f"confirm_yes_{lead_id}", use_container_width=True):
                delete_lead(lead_id)
                st.session_state.selected_lead_id = None
                st.session_state.confirm_delete_id = None
                st.success(f"'{company}' deleted.")
                st.rerun()
        with no_col:
            if st.button("Cancel", key=f"confirm_no_{lead_id}", use_container_width=True):
                st.session_state.confirm_delete_id = None
                st.rerun()


def show():
    if "selected_lead_id" not in st.session_state:
        st.session_state.selected_lead_id = None
    if "show_add_form" not in st.session_state:
        st.session_state.show_add_form = False

    header_col, button_col = st.columns([5, 1])
    with header_col:
        st.subheader("Leads")
    with button_col:
        if st.button("+ Add lead", use_container_width=True):
            st.session_state.show_add_form = not st.session_state.show_add_form

    if st.session_state.show_add_form:
        _render_add_lead_form()
        st.markdown("<div style='margin-bottom:8px;'></div>", unsafe_allow_html=True)

    leads = get_all_leads() + _build_sample_leads()

    list_col, detail_col = st.columns([1.2, 1.3])
    with list_col:
        _render_search_list(leads)
    with detail_col:
        with st.container(height=520, border=True):
            _render_detail_panel()