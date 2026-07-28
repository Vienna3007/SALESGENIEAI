from .schemas import ScoreRequest


def calculate_score(data: ScoreRequest):

    score = 0
    reasons = []

    # Company Size
    if data.employees >= 1000:
        score += 35
        reasons.append("Large enterprise")
    elif data.employees >= 500:
        score += 25
        reasons.append("Medium-large company")
    elif data.employees >= 100:
        score += 15
        reasons.append("Growing company")
    else:
        score += 5
        reasons.append("Small company")

    # Industry
    tech_industries = [
        "Technology",
        "Software",
        "IT",
        "Artificial Intelligence",
        "Cloud",
        "SaaS"
    ]

    if any(i.lower() in data.industry.lower() for i in tech_industries):
        score += 30
        reasons.append("Technology-focused industry")
    else:
        score += 10
        reasons.append("Non-technology industry")

    # Revenue
    revenue = data.revenue.lower()

    if "billion" in revenue:
        score += 35
        reasons.append("High annual revenue")
    elif "million" in revenue:
        score += 25
        reasons.append("Moderate annual revenue")
    else:
        score += 10
        reasons.append("Limited revenue information")

    score = min(score, 100)

    if score >= 80:
        category = "Hot Lead"
    elif score >= 60:
        category = "Warm Lead"
    else:
        category = "Cold Lead"

    return {
        "company": data.company_name,
        "lead_score": score,
        "category": category,
        "reasons": reasons
    }