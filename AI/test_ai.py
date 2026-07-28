from AI_LLM.company_analysis import analyze_company
from AI_LLM.email_generator import generate_email
from AI_LLM.lead_scoring import calculate_score
from AI_LLM.meeting_summary import generate_summary
from AI_LLM.dashboard import get_dashboard_stats

from AI_LLM.schemas import (
    CompanyRequest,
    EmailRequest,
    ScoreRequest,
    SummaryRequest
)

print("========== COMPANY ANALYSIS ==========")

company = CompanyRequest(
    company_name="Infosys",
    industry="IT Services",
    employees=317000,
    revenue="19 Billion USD",
    description="Global IT consulting and AI company."
)

print(analyze_company(company))

print("\n========== LEAD SCORING ==========")

score = ScoreRequest(
    company_name="Infosys",
    industry="Technology",
    employees=7000,
    revenue="19 Billion USD"
)

print(calculate_score(score))

print("\n========== EMAIL ==========")

email = EmailRequest(
    company_name="Infosys",
    industry="IT",
    contact_name="Rajesh",
    insights="Strong AI transformation initiatives."
)

print(generate_email(email))

print("\n========== SUMMARY ==========")

meeting = SummaryRequest(
    transcript="""
Customer wants AI automation.
Budget approval next week.
Demo scheduled on Friday.
"""
)

print(generate_summary(meeting))

print("\n========== DASHBOARD ==========")

print(get_dashboard_stats())