from .schemas import ScoreRequest


def calculate_score(data: ScoreRequest):

    score = 0
    reasons = []

    # Company Size
    size = data.company_size.lower()

    if "enterprise" in size:
        score += 25
        reasons.append("Enterprise organization")

    elif "large" in size:
        score += 20
        reasons.append("Large company")

    elif "medium" in size:
        score += 15
        reasons.append("Medium-sized company")

    else:
        score += 10

    # Buying Probability

    buying = data.buying_probability.lower()

    if "high" in buying:
        score += 25
        reasons.append("High buying probability")

    elif "medium" in buying:
        score += 15

    else:
        score += 5

    # Growth Potential

    growth = data.growth_potential.lower()

    if "high" in growth:
        score += 20
        reasons.append("High growth potential")

    elif "medium" in growth:
        score += 10

    # Technology Maturity

    tech = data.technology_maturity.lower()

    if "advanced" in tech:
        score += 15

    elif "modern" in tech:
        score += 10

    # Market Position

    market = data.market_position.lower()

    if "leader" in market:
        score += 15

    elif "strong" in market:
        score += 10

    score = min(score, 100)

    if score >= 80:
        category = "Hot Lead"

    elif score >= 60:
        category = "Warm Lead"

    else:
        category = "Cold Lead"

    return {

        "lead_score": score,

        "category": category,

        "reasons": reasons

    }