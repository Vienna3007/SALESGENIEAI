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
    industry: str
    employees: int
    revenue: str


class SummaryRequest(BaseModel):
    transcript: str