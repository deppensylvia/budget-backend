from fastapi import FastAPI
from .database import engine
from . import models
from .routers import expenses
from fastapi.middleware.cors import CORSMiddleware

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(expenses.router, prefix="/api", tags=["expenses", "incomes"])

@app.get("/")
def root():
    return {"message": "Welcome to the Expense Tracker API"}
