# Start venv every time a new terminal starts

    source .venv/Scripts/activate 
with GitBash

    .venv\Scripts\Activate.ps1 
for regular windows

use 
    deactivatve
when done working in venv


# Install requirements
    pip install -r requirements.txt

# to see swagger docs add /docs or /redoc for an alternative view
# and /openapi.json to see the raw json

Project steps:

Part 1
1. Expense tracking
    - Create expense item schema
    - Create expense group schema
2. Income tracking
    - Create income item schema
3. Savings Goals
    - Create savings item schema 
        - Sinking fund or emergency fund?
4. Recurring Costs
    - Creating recurring item schema

For each item:
 - GET/POST/UPDATE/DELETE
 - Add controller logic
Part 2
1. Monthly Budget
2. Dashboard
3. Checklist

Part 3
1. End of Month Review
2. End of Year Review

uvicorn app.main:app --reload #run this first
docker-compose up --build #build this after

docker-compose up -d #(local postgres)

