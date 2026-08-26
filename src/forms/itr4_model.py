"""Data models for ITR4 form"""

from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum
from datetime import date


class IncomeType(str, Enum):
    """Types of income sources"""
    SALARY = "salary"
    BUSINESS = "business"
    PROFESSIONAL = "professional"
    CAPITAL_GAINS = "capital_gains"
    HOUSE_PROPERTY = "house_property"
    OTHER = "other"


class IncomeSource(BaseModel):
    """Model for income sources"""
    income_type: IncomeType
    amount: float = Field(gt=0, description="Income amount in INR")
    description: Optional[str] = None
    
    @validator('amount')
    def validate_amount(cls, v):
        if v < 0:
            raise ValueError('Amount must be positive')
        return round(v, 2)


class Deduction(BaseModel):
    """Model for deductions"""
    name: str
    amount: float = Field(gt=0, description="Deduction amount in INR")
    section: str = Field(..., description="Income Tax Act Section (e.g., '80C')")
    
    @validator('amount')
    def validate_amount(cls, v):
        if v < 0:
            raise ValueError('Deduction must be positive')
        return round(v, 2)


class PersonalDetails(BaseModel):
    """Personal information of the taxpayer"""
    pan: str = Field(..., description="Permanent Account Number")
    full_name: str
    date_of_birth: date
    address: str
    phone: str
    email: str
    aadhaar: Optional[str] = None
    
    @validator('pan')
    def validate_pan(cls, v):
        # Basic PAN validation (format: AAAAA0000A)
        if len(v) != 10:
            raise ValueError('PAN must be 10 characters')
        return v.upper()


class ITR4Form(BaseModel):
    """Complete ITR4 Form Model"""
    personal_details: PersonalDetails
    financial_year: str = Field(..., description="FY in format YYYY-YY (e.g., 2023-24)")
    income_sources: List[IncomeSource] = []
    deductions: List[Deduction] = []
    gross_income: float = 0.0
    total_deductions: float = 0.0
    taxable_income: float = 0.0
    tax_liability: float = 0.0
    
    def add_income(self, income: IncomeSource):
        """Add an income source"""
        self.income_sources.append(income)
        self.update_totals()
    
    def add_deduction(self, deduction: Deduction):
        """Add a deduction"""
        self.deductions.append(deduction)
        self.update_totals()
    
    def update_totals(self):
        """Recalculate gross income and deductions"""
        self.gross_income = sum(income.amount for income in self.income_sources)
        self.total_deductions = sum(ded.amount for ded in self.deductions)
        self.taxable_income = max(0, self.gross_income - self.total_deductions)
    
    def to_dict(self):
        """Convert to dictionary"""
        return self.model_dump()
    
    def to_json(self):
        """Convert to JSON string"""
        return self.model_dump_json(indent=2)


__all__ = ["ITR4Form", "IncomeSource", "Deduction", "PersonalDetails", "IncomeType"]
