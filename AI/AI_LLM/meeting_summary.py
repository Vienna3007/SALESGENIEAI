from .config import client
from .prompts import SUMMARY_PROMPT
from .schemas import SummaryRequest


def build_prompt(data: SummaryRequest):

    return SUMMARY_PROMPT.format(
        transcript=data.transcript
    )


def generate_summary(data: SummaryRequest):

    prompt = build_prompt(data)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "summary": response.text
    }