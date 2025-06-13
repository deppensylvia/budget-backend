from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import database
from .. import models, schema

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/incomes", response_model=list[schema.IncomeResponse])
def get_incomes(db: Session = Depends(get_db)):
    return db.query(models.Income).all()

@router.get("/incomes/{income_id}", response_model=schema.IncomeResponse)
def get_income(income_id: str, db: Session = Depends(get_db)):
    db_income = db.query(models.Income).filter(models.Income.id == income_id).first()
    if not db_income:
        return {"error": "Income not found"}
    return db_income

@router.post("/incomes", response_model=schema.IncomeResponse, status_code=201)
def create_income(income: schema.IncomeCreate, db: Session = Depends(get_db)):
    db_income = models.Income(**income.model_dump())
    db.add(db_income)
    db.commit()
    db.refresh(db_income)
    return db_income

@router.put("/incomes/{income_id}", response_model=schema.IncomeResponse)
def update_income(income_id: str, income: schema.IncomeCreate, db: Session = Depends(get_db)):
    db_income = db.query(models.Income).filter(models.Income.id == income_id).first()
    if not db_income:
        return {"error": "Income not found"}
    
    for key, value in income.model_dump().items():
        setattr(db_income, key, value)
    
    db.commit()
    db.refresh(db_income)
    return db_income

@router.delete("/incomes/{income_id}", status_code=204)
def delete_income(income_id: str, db: Session = Depends(get_db)):
    db_income = db.query(models.Income).filter(models.Income.id == income_id).first()
    if not db_income:
        return {"error": "Income not found"}

    db.delete(db_income)
    db.commit()
    return {"message": "Income deleted successfully"}