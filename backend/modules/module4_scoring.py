from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/score",
    tags=["Lead Scoring"]
)

class ScoreRequest(BaseModel):
    company_name: str
    industry: str
    employees: int
    revenue: str

@router.post("/calculate")
def calculate_score(data: ScoreRequest):

    score = 40

    if data.employees >= 500:
        score += 20

    if "Technology" in data.industry:
        score += 20

    if "Billion" in data.revenue:
        score += 20

    score = min(score, 100)

    if score >= 80:
        category = "Hot Lead"
    elif score >= 60:
        category = "Warm Lead"
    else:
        category = "Cold Lead"

    return {
        "company": data.company_name,
        "lead_score": score,
        "category": category,
        "reason":
        "Calculated using company size, industry and revenue."
    }