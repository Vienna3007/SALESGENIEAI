from AI_LLM.sales_pipeline import process_company
from AI_LLM.schemas import CompanyRequest

company = CompanyRequest(
    company_name="Infosys",
    industry="IT Services",
    employees=317000,
    revenue="19 Billion USD",
    description="Global AI consulting company."
)

result = process_company(company)

print(result)