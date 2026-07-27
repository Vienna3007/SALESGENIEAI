import requests

API_BASE = "http://127.0.0.1:8000"

def _get_id(lead_json):
    """Handles either 'id' or 'lead_id' as the backend's key name."""
    return lead_json.get("id", lead_json.get("lead_id"))

def _to_tuple(lead_json):
    """
    Converts the backend's JSON shape into the same tuple shape
    your Streamlit modules already expect:
    (lead_id, company_name, industry, contact_name, email, phone, lead_status, created_at)
    """
    return (
        _get_id(lead_json),
        lead_json.get("company", ""),
        lead_json.get("industry", ""),
        lead_json.get("name", ""),
        lead_json.get("email", ""),
        lead_json.get("phone", ""),
        lead_json.get("status", "New"),
        lead_json.get("created_at", ""),
    )

def init_db():
    # No-op: the backend manages its own database setup.
    pass

def add_lead(company_name, industry, contact_name, email, phone):
    payload = {
        "name": contact_name,
        "company": company_name,
        "email": email,
        "phone": phone,
        "industry": industry,
        "status": "New",
        "notes": "",
    }
    response = requests.post(f"{API_BASE}/leads/", json=payload)
    response.raise_for_status()
    return response.json()

def update_lead(lead_id, company_name, industry, contact_name, email, phone):
    payload = {
        "name": contact_name,
        "company": company_name,
        "email": email,
        "phone": phone,
        "industry": industry,
        "status": "New",
        "notes": "",
    }
    response = requests.put(f"{API_BASE}/leads/{lead_id}", json=payload)
    response.raise_for_status()
    return response.json()

def get_all_leads():
    response = requests.get(f"{API_BASE}/leads/")
    response.raise_for_status()
    leads_json = response.json()
    return [_to_tuple(lead) for lead in leads_json]

def get_lead_by_id(lead_id):
    response = requests.get(f"{API_BASE}/leads/{lead_id}")
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return _to_tuple(response.json())

def find_duplicate_lead(email, phone):
    """
    The backend has no built-in duplicate check, so we fetch all leads
    and check email/phone here, same logic as before.
    """
    all_leads = get_all_leads()
    for lead in all_leads:
        if lead[4].lower() == email.strip().lower() or lead[5] == phone.strip():
            return lead
    return None

def delete_lead(lead_id):
    response = requests.delete(f"{API_BASE}/leads/{lead_id}")
    response.raise_for_status()

def update_lead_status(lead_id, status):
    # Fetch current lead first so we don't overwrite other fields
    current = get_lead_by_id(lead_id)
    if current is None:
        return
    payload = {
        "name": current[3],
        "company": current[1],
        "email": current[4],
        "phone": current[5],
        "industry": current[2],
        "status": status,
        "notes": "",
    }
    response = requests.put(f"{API_BASE}/leads/{lead_id}", json=payload)
    response.raise_for_status()