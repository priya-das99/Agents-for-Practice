from pydantic import BaseModel
from typing import List


class Budget(BaseModel):
    needs: float
    wants: float
    savings: float
    tips: List[str]


class Investments(BaseModel):
    emergency_fund: str
    mutual_funds: List[str]
    fixed_deposits: List[str]
    stocks: List[str]
    notes: List[str]


class Risk(BaseModel):
    risk_level: str
    reasons: List[str]
    warnings: List[str]
    safer_options: List[str]


class FinanceResponse(BaseModel):
    budget: Budget
    investments: Investments
    risk: Risk