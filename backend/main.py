from fastapi import FastAPI
from database.connection import engine, Base
from modules import module1_leads

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SalesGenie AI", description="AI-powered Sales Assistant", version="1.0")

app.include_router(module1_leads.router)

@app.get("/")
def root():
    return {"message": "Welcome to SalesGenie AI 🚀"}