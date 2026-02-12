import numpy as np
import pandas as pd
from fastapi import FastAPI
from schema import Loan

app = FastAPI()

@app.get("/")
def home():
    return{"message":"hello"}

@app.post("/loan_eligibility")
def check(data:Loan):
    if data.age >= 21 and data.monthly_income >=2000 and data.existing_loans <5000:
         return {"eligible":"true"}
    else:
        return {"eligible":"false"}