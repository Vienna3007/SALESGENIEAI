"""
AI Lead Qualification Engine

Input:
Dictionary containing company information.

Output:
Dictionary containing

- Qualification Score
- Priority
- Growth Potential
- Technology Alignment
- Pain Points
- Sales Strategy
- Reasons

Developed for SalesGenie AI
"""
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_company_insights(company_data):

    required_fields = [
        "company_name",
        "industry",
        "employees",
        "revenue",
        "description"
    ]

    for field in required_fields:
        if field not in company_data:
            raise ValueError(f"Missing field: {field}")


    prompt = f"""
You are an AI Sales Intelligence Assistant.

Analyze the company below.

Company Name: {company_data['company_name']}
Industry: {company_data['industry']}
Employees: {company_data['employees']}
Revenue: {company_data['revenue']}
Description: {company_data['description']}

Return ONLY valid JSON.

Format:

{{
    "qualification_score": 0,
    "priority": "",
    "growth_potential": "",
    "technology_alignment": "",
    "pain_points": [
        "",
        "",
        ""
    ],
    "sales_strategy": "",
    "reasons": [
        "",
        "",
        ""
    ]
}}

Rules:

qualification_score:
Return a number from 0-100.

priority:
Choose only one:
Hot
Warm
Cold

growth_potential:
Choose only one:
High
Medium
Low

technology_alignment:
Choose only one:
Excellent
Good
Average
Poor

pain_points:
Maximum 3 points.

reasons:
Maximum 3 reasons.

sales_strategy:
Maximum 2 sentences.

Do not return markdown.

Do not explain.

Return JSON only.
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)