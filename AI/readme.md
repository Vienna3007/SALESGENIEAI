# AI_LLM Module - SalesGenie AI

## Overview

This module contains the complete AI/LLM logic for the SalesGenie AI platform.

The AI layer is completely independent of the frontend and backend. It is designed to be plugged into the backend through API endpoints or service calls.

Current capabilities include:

- Company Analysis (Gemini AI)
- AI-based Lead Scoring
- Personalized Sales Email Generation
- Meeting Summary Generation
- Dashboard Analytics
- End-to-End AI Sales Pipeline

---

# Folder Structure

```
AI_LLM/
│
├── __init__.py
├── integration.py
├── sales_pipeline.py
│
├── company_analysis.py
├── lead_scoring.py
├── email_generator.py
├── meeting_summary.py
├── dashboard.py
│
├── schemas.py
├── prompts.py
├── config.py
└── utils.py
```

---

# Architecture

```
Frontend
      │
      ▼
Backend API
      │
      ▼
SalesGenieAI.process_company()
      │
      ├── Company Analysis
      ├── Lead Scoring
      ├── Email Generation
      ├── Meeting Summary
      │
      ▼
Return Single JSON Response
```

The backend should only call the integration layer.

The backend should **NOT** directly call individual AI modules.

---

# Main Entry Point

Import:

```python
from AI.AI_LLM import SalesGenieAI
```

---

# Processing a Company

Example:

```python
from AI.AI_LLM import SalesGenieAI
from AI.AI_LLM.schemas import CompanyRequest

company = CompanyRequest(
    company_name="Infosys",
    industry="IT Services",
    employees=317000,
    revenue="19 Billion USD",
    description="Global IT consulting company."
)

result = SalesGenieAI.process_company(company)
```

The returned object contains:

```python
{
    "analysis": {...},
    "lead_score": {...},
    "email": {...},
    "meeting_summary": {...}
}
```

---

# Dashboard

Dashboard statistics are generated from backend/database data.

Example:

```python
stats = SalesGenieAI.dashboard(leads)
```

Input:

```python
[
    {
        "score":95
    },
    {
        "score":74
    },
    {
        "score":52
    }
]
```

Output:

```python
{
    "total_leads":3,
    "hot_leads":1,
    "warm_leads":1,
    "cold_leads":1,
    "average_score":73.67
}
```

---

# Backend Integration

Backend flow:

1. Receive company details from Frontend
2. Create CompanyRequest object
3. Call:

```python
SalesGenieAI.process_company(company_request)
```

4. Return the response to the frontend.

No AI logic needs to be implemented inside the backend.

---

# Meeting Summary

Meeting summaries require a transcript.

Example:

```python
SummaryRequest(
    transcript="Meeting transcript..."
)
```

The module returns:

- Meeting Summary
- Action Items
- Next Steps
- Follow-up Points

---

# Environment Variables

Create a `.env` file inside the project.

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# Required Python Packages

```
google-genai
python-dotenv
pydantic
```

---

# Design Principles

- Modular AI architecture
- Backend independent
- Frontend independent
- Reusable components
- Single integration point
- Easy future extension

---

# Current AI Modules

### Company Analysis

Uses Gemini AI to analyze companies and returns structured JSON containing:

- Company Size
- Market Position
- Technology Maturity
- Growth Potential
- Buying Probability
- Opportunities
- Risks
- Pain Points
- Competitive Advantages

---

### Lead Scoring

Uses the Company Analysis output to calculate:

- Lead Score
- Lead Category
- Scoring Reasons

---

### Email Generator

Generates personalized cold outreach emails using:

- Company Analysis
- Company Insights
- Industry Information

---

### Meeting Summary

Generates:

- Meeting Summary
- Action Items
- Next Steps
- Follow-up Email Points

---

### Dashboard

Computes dashboard metrics dynamically from backend-provided lead data, including:

- Total Leads
- Hot Leads
- Warm Leads
- Cold Leads
- Average Lead Score

---

# Notes for Integration

- This module does not directly connect to the database.
- Database operations should remain inside the backend.
- Backend is responsible for passing the required data into the AI module.
- Dashboard functions expect processed lead data from the backend.
- The AI module only handles AI logic and business intelligence.

---

# Future Enhancements

Possible future improvements:

- CRM Integration (Salesforce, HubSpot, Zoho)
- RAG-based Company Knowledge
- AI Chat Assistant
- Multi-Agent Workflow using LangGraph
- Vector Database Integration
- Conversation Memory
- Lead Recommendation Engine

---

Developed as part of the SalesGenie AI Internship Project.

AI Module Owner:
**Pydi Sri Vaishnavi**
