from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import relationship
from database.connection import Base


class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String(100), nullable=False)
    industry = Column(String(100))
    website = Column(String(100))
    location = Column(String(100))
    employees = Column(Integer)


class Contact(Base):
    __tablename__ = "contacts"

    contact_id = Column(Integer, primary_key=True, index=True)
    company_id = Column(Integer, ForeignKey("companies.company_id"))
    contact_name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    designation = Column(String(100))


from sqlalchemy import Column, Integer, String, Text, DateTime, Date, ForeignKey
from sqlalchemy.sql import func
from database.connection import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    company = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    industry = Column(String(100), nullable=True)
    status = Column(String(50), default="New")
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


# ================= Module 2 =================

class LeadStage(Base):
    __tablename__ = "lead_stage"

    stage_id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"), nullable=False)
    stage_name = Column(String(50), nullable=False)
    updated_date = Column(Date, nullable=False)


class AIInsight(Base):
    __tablename__ = "ai_insights"

    insight_id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id"))
    lead_score = Column(Integer)
    conversion_probability = Column(DECIMAL(5,2))
    recommendation = Column(String(255))