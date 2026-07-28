import json

from .config import client
from .prompts import COMPANY_ANALYSIS_PROMPT
from .schemas import CompanyRequest
from .utils import clean_json


def build_prompt(data: CompanyRequest):

    return COMPANY_ANALYSIS_PROMPT.format(
        company_name=data.company_name,
        industry=data.industry,
        employees=data.employees,
        revenue=data.revenue,
        description=data.description
    )


def analyze_company(data: CompanyRequest):

    prompt = build_prompt(data)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    try:

        return clean_json(response.text)

    except json.JSONDecodeError:

        return {
            "error": "Gemini returned invalid JSON.",
            "raw_response": response.text
        }