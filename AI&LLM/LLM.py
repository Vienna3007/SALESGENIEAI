import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_company_insights(company_data):

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
    "pain_points": [],
    "sales_strategy": "",
    "reasons": []
}}

Rules:
- qualification_score: Number from 0-100
- priority: Hot, Warm or Cold
- growth_potential: High, Medium or Low
- technology_alignment: Excellent, Good, Average or Poor
- Maximum 3 pain_points
- Maximum 3 reasons
- sales_strategy: Maximum 2 sentences

Return JSON only.
"""

    response = model.generate_content(prompt)

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)