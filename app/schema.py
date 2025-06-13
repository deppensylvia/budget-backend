from pydantic import BaseModel
from datetime import date

class ExpenseCreate(BaseModel):
    id: str

    item: str
    budget_category: str
    cost: float
    show_in_budget: bool = True
    purchase_date: date 
    purchase_source: str
    notes: str = None

class ExpenseResponse(ExpenseCreate):
    id: str

    class Config:
        from_attributes = True
