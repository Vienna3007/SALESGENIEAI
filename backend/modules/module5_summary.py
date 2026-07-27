from fastapi import APIRouter
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

router = APIRouter(
    prefix="/summary",
    tags=["Meeting Summary"]
)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class SummaryRequest(BaseModel):
    transcript: str


@router.post("/generate")
def generate_summary(data: SummaryRequest):

    prompt = f"""
You are an AI Sales Assistant.

Read the meeting transcript below.

{data.transcript}

Generate:

1. Meeting Summary
2. Action Items
3. Next Steps
4. Follow-up Email Points

Return in clean text.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "summary": response.text
    }