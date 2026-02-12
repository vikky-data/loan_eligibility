from pydantic import BaseModel

class Loan(BaseModel):
    age : int
    monthly_income : float
    existing_loans : float 



