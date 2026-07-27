import os
import json
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key=api_key)

router = APIRouter(
    prefix="/analysis",
    tags=["Company Analysis"]
)

class CompanyRequest(BaseModel):
    company_name: str
    industry: str
    employees: int
    revenue: str
    description: str


def build_prompt(data: CompanyRequest):
    return f"""
You are an expert AI Sales Intelligence Analyst.

Analyze the following company.

Company Name:
{data.company_name}

Industry:
{data.industry}

Employees:
{data.employees}

Revenue:
{data.revenue}

Description:
{data.description}

Return ONLY valid JSON.

{{
  "company_name":"",
  "industry":"",
  "company_size":"",
  "market_position":"",
  "technology_maturity":"",
  "growth_potential":"",
  "buying_probability":"",
  "recommended_strategy":"",
  "pain_points":["","",""],
  "competitive_advantages":["","",""],
  "tech_stack":["","",""],
  "opportunities":["","",""],
  "risks":["","",""],
  "summary":""
}}
"""


def generate_company_analysis(data: CompanyRequest):

    prompt = build_prompt(data)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    result = response.text.replace("```json", "").replace("```", "").strip()

    return json.loads(result)


@router.post("/analyze-company")
def analyze_company(request: CompanyRequest):

    analysis = generate_company_analysis(request)

    return {
        "status": "success",
        "company": request.company_name,
        "analysis": analysis
    }