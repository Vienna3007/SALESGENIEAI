from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime

from database.connection import get_db
from database.models import Lead

router = APIRouter(prefix="/leads", tags=["Leads"])


# ---------------- Pydantic Schemas ----------------

class LeadCreate(BaseModel):
    name: str
    company: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    industry: Optional[str] = None
    status: Optional[str] = "New"
    notes: Optional[str] = None


class LeadUpdate(BaseModel):
    name: Optional[str] = None
    company: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    industry: Optional[str] = None
    status: Optional[str] = None
    notes: Optional[str] = None


class LeadResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    company: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    industry: Optional[str]
    status: Optional[str]
    notes: Optional[str]
    created_at: datetime


# ---------------- 1. Add Lead ----------------

@router.post("/", response_model=LeadResponse)
def add_lead(lead: LeadCreate, db: Session = Depends(get_db)):

    if lead.email:
        existing = db.query(Lead).filter(Lead.email == lead.email).first()
        if existing:
            raise HTTPException(
                status_code=400,
                detail=f"A lead with email '{lead.email}' already exists (id={existing.id})"
            )

    new_lead = Lead(**lead.model_dump())

    db.add(new_lead)
    db.commit()
    db.refresh(new_lead)

    return new_lead


# ---------------- 2. Get All Leads ----------------

@router.get("/", response_model=list[LeadResponse])
def get_all_leads(
    db: Session = Depends(get_db),
    name: Optional[str] = Query(None),
    company: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100)
):

    query = db.query(Lead)

    if name:
        query = query.filter(Lead.name.ilike(f"%{name}%"))

    if company:
        query = query.filter(Lead.company.ilike(f"%{company}%"))

    if status:
        query = query.filter(Lead.status == status)

    return query.offset(skip).limit(limit).all()


# ---------------- 3. Get Lead By ID ----------------

@router.get("/{lead_id}", response_model=LeadResponse)
def get_lead(lead_id: int, db: Session = Depends(get_db)):

    lead = db.query(Lead).filter(Lead.id == lead_id).first()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    return lead


# ---------------- 4. Update Lead ----------------

@router.put("/{lead_id}", response_model=LeadResponse)
def update_lead(
    lead_id: int,
    updated_data: LeadUpdate,
    db: Session = Depends(get_db)
):

    lead = db.query(Lead).filter(Lead.id == lead_id).first()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    update_fields = updated_data.model_dump(exclude_unset=True)

    if "email" in update_fields and update_fields["email"]:
        existing = db.query(Lead).filter(
            Lead.email == update_fields["email"],
            Lead.id != lead_id
        ).first()

        if existing:
            raise HTTPException(
                status_code=400,
                detail=f"Email '{update_fields['email']}' is already used by lead id={existing.id}"
            )

    for field, value in update_fields.items():
        setattr(lead, field, value)

    db.commit()
    db.refresh(lead)

    return lead


# ---------------- 5. Delete Lead ----------------

@router.delete("/{lead_id}")
def delete_lead(lead_id: int, db: Session = Depends(get_db)):

    lead = db.query(Lead).filter(Lead.id == lead_id).first()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    db.delete(lead)
    db.commit()

    return {"message": f"Lead with id {lead_id} deleted successfully"}