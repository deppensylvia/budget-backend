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

@router.get("/expenses", response_model=list[schema.ExpenseResponse])
def get_expenses(db: Session = Depends(get_db)):
    return db.query(models.Expense).all()

@router.get("/expenses/{expense_id}", response_model=schema.ExpenseResponse)
def get_expense(expense_id: str, db: Session = Depends(get_db)):
    db_expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not db_expense:
        return {"error": "Expense not found"}
    return db_expense

@router.post("/expenses", response_model=schema.ExpenseResponse, status_code=201)
def create_expense(expense: schema.ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = models.Expense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.put("/expenses/{expense_id}", response_model=schema.ExpenseResponse)
def update_expense(expense_id: str, expense: schema.ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not db_expense:
        return {"error": "Expense not found"}
    
    for key, value in expense.model_dump().items():
        setattr(db_expense, key, value)
    
    db.commit()
    db.refresh(db_expense)
    return db_expense

@router.delete("/expenses/{expense_id}", status_code=204)
def delete_expense(expense_id: str, db: Session = Depends(get_db)):
    db_expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()
    if not db_expense:
        return {"error": "Expense not found"}

    db.delete(db_expense)
    db.commit()
    return {"message": "Expense deleted successfully"}