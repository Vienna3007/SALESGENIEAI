from pydantic import BaseModel


class CompanyRequest(BaseModel):
    company_name: str
    industry: str
    employees: int
    revenue: str
    description: str


class EmailRequest(BaseModel):
    company_name: str
    industry: str
    contact_name: str
    insights: str


class ScoreRequest(BaseModel):

    company_name: str

    company_size: str

    market_position: str

    technology_maturity: str

    growth_potential: str

    buying_probability: str


class SummaryRequest(BaseModel):
    transcript: str