import json
from llm import generate_company_insights

companies = [
    {
        "company_name": "Infosys",
        "industry": "Information Technology",
        "employees": 340000,
        "revenue": "18 Billion USD",
        "description": "Provides consulting, cloud, AI, and digital transformation services."
    },
    {
        "company_name": "Tesla",
        "industry": "Automotive",
        "employees": 140000,
        "revenue": "96 Billion USD",
        "description": "Electric vehicle manufacturer focusing on AI and autonomous driving."
    },
    {
        "company_name": "Zomato",
        "industry": "Food Delivery",
        "employees": 7000,
        "revenue": "1.5 Billion USD",
        "description": "Online food delivery and restaurant discovery platform."
    }
]

for company in companies:

    print("\n" + "=" * 60)
    print(f"Company: {company['company_name']}")
    print("=" * 60)

    result = generate_company_insights(company)

    print(json.dumps(result, indent=4))