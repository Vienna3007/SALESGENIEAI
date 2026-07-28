from .config import client
from .prompts import EMAIL_PROMPT
from .schemas import EmailRequest


def build_prompt(data: EmailRequest):

    return EMAIL_PROMPT.format(
        company_name=data.company_name,
        industry=data.industry,
        contact_name=data.contact_name,
        insights=data.insights
    )


def generate_email(data: EmailRequest):

    prompt = build_prompt(data)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {
        "company": data.company_name,
        "email": response.text
    }