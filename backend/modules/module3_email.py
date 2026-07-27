from fastapi import APIRouter
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

router = APIRouter(
    prefix="/email",
    tags=["AI Email"]
)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class EmailRequest(BaseModel):
    company_name: str
    industry: str
    contact_name: str
    insights: str

@router.post("/generate")
def generate_email(data: EmailRequest):

    prompt = f"""
Generate a professional cold outreach email.

Company: {data.company_name}
Industry: {data.industry}
Contact: {data.contact_name}
Insights: {data.insights}

Keep it under 180 words.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "company": data.company_name,
        "email": response.text
    }