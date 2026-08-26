"""Deduction calculation and validation"""

from typing import Dict, List
from enum import Enum


class DeductionSection(str, Enum):
    """Common deduction sections under Income Tax Act"""
    SECTION_80C = "80C"      # Investment-linked deductions
    SECTION_80CCC = "80CCC"  # Pension scheme
    SECTION_80CCD = "80CCD"  # NPS contributions
    SECTION_80D = "80D"      # Medical insurance
    SECTION_80E = "80E"      # Interest on education loan
    SECTION_80G = "80G"      # Charitable donations
    SECTION_80TTA = "80TTA"  # Savings account interest
    SECTION_80TTB = "80TTB"  # Interest on deposits (seniors)


class DeductionCalculator:
    """Calculate and validate deductions"""
    
    # Deduction limits for FY 2023-24
    DEDUCTION_LIMITS = {
        DeductionSection.SECTION_80C: 150000,
        DeductionSection.SECTION_80CCC: 150000,
        DeductionSection.SECTION_80CCD: 50000,
        DeductionSection.SECTION_80D: 100000,
        DeductionSection.SECTION_80E: float('inf'),  # No limit
        DeductionSection.SECTION_80G: float('inf'),  # No limit
        DeductionSection.SECTION_80TTA: 10000,
        DeductionSection.SECTION_80TTB: 50000,
    }
    
    def __init__(self):
        """Initialize deduction calculator"""
        self.deductions: Dict[str, float] = {}
    
    def add_deduction(self, section: str, amount: float, description: str = ""):
        """Add a deduction"""
        if section not in self.DEDUCTION_LIMITS:
            raise ValueError(f"Unknown section: {section}")
        
        if amount < 0:
            raise ValueError("Deduction amount cannot be negative")
        
        key = f"{section}_{description}"
        self.deductions[key] = amount
    
    def validate_deduction(self, section: str, amount: float) -> bool:
        """Validate if deduction is within limits"""
        if section not in self.DEDUCTION_LIMITS:
            return False
        
        limit = self.DEDUCTION_LIMITS[section]
        return amount <= limit
    
    def get_total_deductions(self) -> float:
        """Calculate total deductions"""
        return sum(self.deductions.values())
    
    def get_deductions_by_section(self) -> Dict[str, float]:
        """Get deductions grouped by section"""
        grouped = {}
        for key, amount in self.deductions.items():
            section = key.split('_')[0]
            if section not in grouped:
                grouped[section] = 0
            grouped[section] += amount
        return grouped
    
    def get_deduction_summary(self) -> Dict:
        """Get detailed deduction summary"""
        summary = {}
        for section in DeductionSection:
            limit = self.DEDUCTION_LIMITS[section.value]
            claimed = sum(
                v for k, v in self.deductions.items() 
                if k.startswith(section.value)
            )
            summary[section.value] = {
                "limit": limit,
                "claimed": claimed,
                "remaining": max(0, limit - claimed),
                "percentage_used": (claimed / limit * 100) if limit != float('inf') else 0
            }
        return summary


__all__ = ["DeductionCalculator", "DeductionSection"]
