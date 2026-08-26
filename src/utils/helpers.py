"""Helper functions"""

from datetime import datetime
from typing import Union


def format_currency(amount: Union[int, float], currency: str = "INR") -> str:
    """Format amount as currency"""
    if currency == "INR":
        return f"₹{amount:,.2f}"
    else:
        return f"{amount:,.2f} {currency}"


def parse_date(date_string: str, format: str = "%Y-%m-%d") -> datetime:
    """Parse date string to datetime object"""
    return datetime.strptime(date_string, format)


def get_financial_year(date_obj: datetime = None) -> str:
    """Get financial year for a given date (default: today)"""
    if date_obj is None:
        date_obj = datetime.now()
    
    year = date_obj.year
    month = date_obj.month
    
    if month >= 4:  # Financial year starts April 1
        fy_start = year
        fy_end = year + 1
    else:
        fy_start = year - 1
        fy_end = year
    
    return f"{fy_start}-{str(fy_end)[-2:]}"


def round_to_nearest_rupee(amount: float) -> float:
    """Round amount to nearest rupee (50 paise rule)"""
    if amount % 1 >= 0.5:
        return round(amount)
    else:
        return int(amount)


__all__ = ["format_currency", "parse_date", "get_financial_year", "round_to_nearest_rupee"]
