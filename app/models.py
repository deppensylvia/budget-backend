from .database import Base
from sqlalchemy import Column, Boolean, String, DateTime, Float

class Expense(Base):
    __tablename__ = "Expenses"

    id = Column(String, primary_key=True, index=True)
    item = Column(String)
    budget_category = Column(String)
    cost = Column(Float)
    show_in_budget = Column(Boolean, default=True)
    purchase_date = Column(DateTime)
    purchase_source = Column(String)
    notes = Column(String, nullable=True)

    def __repr__(self):
        return f"<Expense(id={self.id}, description='{self.item}', amount={self.cost}, date={self.purchase_date})>"
    
class Income(Base):
    __tablename__ = "Incomes"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    source = Column(String)
    amount = Column(Float)
    received_date = Column(DateTime)
    notes = Column(String, nullable=True)

    def __repr__(self):
        return f"<Income(id={self.id}, name='{self.name}', source='{self.source}', amount={self.amount}, date={self.received_date})>"