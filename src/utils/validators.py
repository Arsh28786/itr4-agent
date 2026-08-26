"""Form validation utilities"""

import re
from typing import Tuple


class FormValidator:
    """Validate form fields and data"""
    
    @staticmethod
    def validate_pan(pan: str) -> Tuple[bool, str]:
        """
        Validate PAN format
        Format: AAAAA0000A (5 letters, 4 digits, 1 letter)
        """
        pattern = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
        if re.match(pattern, pan):
            return True, "Valid PAN"
        return False, "Invalid PAN format"
    
    @staticmethod
    def validate_email(email: str) -> Tuple[bool, str]:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True, "Valid email"
        return False, "Invalid email format"
    
    @staticmethod
    def validate_phone(phone: str) -> Tuple[bool, str]:
        """Validate Indian phone number"""
        pattern = r'^[6-9]\d{9}$'
        if re.match(pattern, phone.replace('-', '').replace(' ', '')):
            return True, "Valid phone number"
        return False, "Invalid phone number format"
    
    @staticmethod
    def validate_aadhaar(aadhaar: str) -> Tuple[bool, str]:
        """Validate Aadhaar format (12 digits)"""
        pattern = r'^\d{12}$'
        if re.match(pattern, aadhaar):
            return True, "Valid Aadhaar"
        return False, "Invalid Aadhaar format"
    
    @staticmethod
    def validate_financial_year(fy: str) -> Tuple[bool, str]:
        """
        Validate financial year format
        Format: YYYY-YY (e.g., 2023-24)
        """
        pattern = r'^\d{4}-\d{2}$'
        if re.match(pattern, fy):
            try:
                start_year = int(fy.split('-')[0])
                end_year = int(fy.split('-')[1])
                if end_year == start_year % 100 + 1:
                    return True, "Valid financial year"
                return False, "Invalid financial year range"
            except:
                return False, "Invalid financial year format"
        return False, "Invalid financial year format"


__all__ = ["FormValidator"]
