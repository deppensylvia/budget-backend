from .database import Base
from sqlalchemy import Column, Boolean, String, DateTime, Float

class Expense(Base):
    __tablename__ = "Expenses"

    id = Column(String, primary_key=True, index=True)
    expense_name = Column(String)
    category = Column(String)
    cost = Column(Float)
    show_in_budget = Column(Boolean, default=True)
    purchase_date = Column(DateTime)
    purchase_source = Column(String)
    notes = Column(String, nullable=True)

    def __repr__(self):
        return f"<Expense(id={self.id}, description='{self.expense_name}', amount={self.cost}, date={self.purchase_date})>"
    
class Income(Base):
    __tablename__ = "Incomes"

    id = Column(String, primary_key=True, index=True)
    income_name = Column(String)
    source = Column(String)
    amount = Column(Float)
    received_date = Column(DateTime)
    notes = Column(String, nullable=True)

    def __repr__(self):
        return f"<Income(id={self.id}, name='{self.income_name}', source='{self.source}', amount={self.amount}, date={self.received_date})>"