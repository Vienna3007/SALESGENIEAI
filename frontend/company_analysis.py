def analyze_company(company_name, industry):
    industry_insights = {
        "technology": "High digital adoption, likely open to AI/automation tools.",
        "finance": "Strong compliance needs; values security and reliability.",
        "healthcare": "Focus on data privacy, efficiency and patient outcomes.",
        "retail": "High interest in customer engagement and CRM automation.",
        "manufacturing": "Interested in process automation and cost reduction.",
    }

    key = (industry or "").lower().strip()
    matched_insight = "General business — evaluate specific needs during discovery call."
    for k, v in industry_insights.items():
        if k in key:
            matched_insight = v
            break

    score = 60
    if any(k in key for k in industry_insights.keys()):
        score += 20
    if len(company_name) > 3:
        score += 5
    score = min(score, 99)

    return {
        "company_name": company_name,
        "industry": industry,
        "insight": matched_insight,
        "qualification_score": score,
        "opportunity": "Cloud Migration / Process Automation" if score > 70 else "Needs further qualification"
    }