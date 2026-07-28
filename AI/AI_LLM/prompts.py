COMPANY_ANALYSIS_PROMPT = """
You are an expert AI Sales Intelligence Analyst.

Analyze the company below.

Company Name:
{company_name}

Industry:
{industry}

Employees:
{employees}

Revenue:
{revenue}

Description:
{description}

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
  "pain_points":[
      "",
      "",
      ""
  ],
  "competitive_advantages":[
      "",
      "",
      ""
  ],
  "tech_stack":[
      "",
      "",
      ""
  ],
  "opportunities":[
      "",
      "",
      ""
  ],
  "risks":[
      "",
      "",
      ""
  ],
  "summary":""
}}
"""


EMAIL_PROMPT = """
Generate a professional cold outreach email.

Company:
{company_name}

Industry:
{industry}

Contact:
{contact_name}

Insights:
{insights}

Requirements:

- Professional
- Personalized
- Mention company insight
- Explain AI Sales Platform
- End with meeting request
- Under 180 words
"""


SUMMARY_PROMPT = """
Read this sales meeting transcript.

{transcript}

Generate

1. Summary

2. Action Items

3. Next Steps

4. Follow-up Email Points
"""