def get_dashboard_stats(leads):

    total = len(leads)

    hot = sum(1 for lead in leads if lead["score"] >= 80)

    warm = sum(1 for lead in leads if 60 <= lead["score"] < 80)

    cold = sum(1 for lead in leads if lead["score"] < 60)

    avg = (
        round(sum(lead["score"] for lead in leads) / total, 2)
        if total else 0
    )

    return {
        "total_leads": total,
        "hot_leads": hot,
        "warm_leads": warm,
        "cold_leads": cold,
        "average_score": avg
    }