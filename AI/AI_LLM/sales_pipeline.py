from .company_analysis import analyze_company
from .lead_scoring import calculate_score
from .email_generator import generate_email
from .meeting_summary import generate_summary

from .schemas import (
    CompanyRequest,
    ScoreRequest,
    EmailRequest,
    SummaryRequest,
)


def process_company(data: CompanyRequest):

    # -----------------------------
    # Step 1: Analyze Company
    # -----------------------------
    analysis = analyze_company(data)

    # -----------------------------
    # Step 2: Calculate Lead Score
    # -----------------------------
    score_input = ScoreRequest(
        company_name=analysis["company_name"],
        company_size=analysis["company_size"],
        market_position=analysis["market_position"],
        technology_maturity=analysis["technology_maturity"],
        growth_potential=analysis["growth_potential"],
        buying_probability=analysis["buying_probability"],
    )

    score = calculate_score(score_input)

    # -----------------------------
    # Step 3: Generate Sales Email
    # -----------------------------
    email_input = EmailRequest(
        company_name=analysis["company_name"],
        industry=analysis["industry"],
        contact_name="Decision Maker",
        insights=analysis["summary"],
    )

    email = generate_email(email_input)

    # -----------------------------
    # Step 4: Generate Meeting Summary
    # -----------------------------
    summary_input = SummaryRequest(
        transcript=f"""
Company: {analysis['company_name']}

Industry: {analysis['industry']}

Company Analysis:
{analysis['summary']}

Lead Category:
{score['category']}

Lead Score:
{score['lead_score']}
"""
    )

    meeting_summary = generate_summary(summary_input)

    # -----------------------------
    # Final Output
    # -----------------------------
    return {
        "analysis": analysis,
        "lead_score": score,
        "email": email,
        "meeting_summary": meeting_summary,
    }