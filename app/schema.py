from pydantic import BaseModel
from datetime import date

class ExpenseCreate(BaseModel):
    id: str
    expense_name: str
    category: str
    cost: float
    show_in_budget: bool = True
    purchase_date: date 
    purchase_source: str
    notes: str = None

class ExpenseResponse(ExpenseCreate):
    id: str

    class Config:
        from_attributes = True

class IncomeCreate(BaseModel):
    id: str
    income_name: str
    amount: float
    received_date: date 
    source: str
    notes: str = None

class IncomeResponse(IncomeCreate):
    id: str

    class Config:
        from_attributes = True
