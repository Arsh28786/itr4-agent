"""Test the ITR4 Agent - Complete Testing Guide"""

# ============================================================================
# HOW TO TEST THE ITR4 AGENT - Comprehensive Guide
# ============================================================================

## 1. SETUP & INSTALLATION

# Clone the repository
git clone https://github.com/Arsh28786/itr4-agent.git
cd itr4-agent

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# ============================================================================
## 2. UNIT TESTING (Using pytest)
# ============================================================================

# Run all tests
pytest tests/

# Run tests with verbose output
pytest tests/ -v

# Run tests with coverage report
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_forms.py

# Run specific test function
pytest tests/test_forms.py::test_create_personal_details

# ============================================================================
## 3. MANUAL TESTING - Form Models
# ============================================================================

from datetime import date
from src.forms.itr4_model import (
    ITR4Form, PersonalDetails, IncomeSource, 
    Deduction, IncomeType
)

# Test 1: Create Personal Details
personal_details = PersonalDetails(
    pan="AAAAA0000A",
    full_name="John Doe",
    date_of_birth=date(1990, 1, 15),
    address="123 Main St, New York, NY",
    phone="9876543210",
    email="john@example.com",
    aadhaar="123456789012"
)
print("✓ Personal Details Created:", personal_details.full_name)

# Test 2: Create ITR4 Form
itr4_form = ITR4Form(
    personal_details=personal_details,
    financial_year="2023-24"
)
print("✓ ITR4 Form Created for FY:", itr4_form.financial_year)

# Test 3: Add Income Sources
salary_income = IncomeSource(
    income_type=IncomeType.SALARY,
    amount=1000000.00,
    description="Annual salary"
)
itr4_form.add_income(salary_income)
print(f"✓ Income Added: ₹{itr4_form.gross_income:,.2f}")

# Test 4: Add Deductions
deduction = Deduction(
    name="Life Insurance Premium",
    amount=150000.00,
    section="80C"
)
itr4_form.add_deduction(deduction)
print(f"✓ Deduction Added. Taxable Income: ₹{itr4_form.taxable_income:,.2f}")

# Test 5: Export Form to JSON
json_output = itr4_form.to_json()
print("✓ Form exported to JSON")
print(json_output[:200] + "...")

# ============================================================================
## 4. MANUAL TESTING - Agent
# ============================================================================

from src.agent.itr4_agent import ITR4Agent

# Test 1: Initialize Agent
agent = ITR4Agent()
print("✓ Agent Initialized")

# Test 2: Start Interview
welcome_msg = agent.start_interview()
print("✓ Interview Started")
print(welcome_msg[:100] + "...")

# Test 3: Create Form with Agent
agent.create_form({
    "pan": "BBBBB1111B",
    "full_name": "Jane Smith",
    "date_of_birth": date(1985, 5, 20),
    "address": "456 Oak Ave, San Francisco, CA",
    "phone": "9123456789",
    "email": "jane@example.com"
})
print("✓ Form Created via Agent")

# Test 4: Add Income via Agent
agent.add_income({
    "income_type": "salary",
    "amount": 1500000,
    "description": "Annual salary"
})
print("✓ Income Added via Agent")

# Test 5: Add Deduction via Agent
agent.add_deduction({
    "name": "Home Loan Interest",
    "amount": 200000,
    "section": "24(b)"
})
print("✓ Deduction Added via Agent")

# Test 6: Get Form Summary
summary = agent.get_form_summary()
print("✓ Form Summary:")
for key, value in summary.items():
    print(f"  {key}: {value}")

# Test 7: Generate Form
generated_form = agent.generate_form()
print("✓ Form Generated")

# Test 8: Export Form
json_export = agent.export_form(format='json')
print("✓ Form Exported to JSON")

# ============================================================================
## 5. MANUAL TESTING - Tax Calculator
# ============================================================================

from src.calculations.tax_calculator import TaxCalculator

# Test 1: Create Calculator
calculator = TaxCalculator(financial_year="2023-24")
print("✓ Tax Calculator Initialized")

# Test 2: Calculate Tax
taxable_income = 1000000
tax_result = calculator.calculate_tax(taxable_income)
print("✓ Tax Calculated:")
print(f"  Taxable Income: ₹{tax_result['taxable_income']:,.2f}")
print(f"  Basic Tax: ₹{tax_result['basic_tax']:,.2f}")
print(f"  Surcharge: ₹{tax_result['surcharge']:,.2f}")
print(f"  Cess: ₹{tax_result['cess']:,.2f}")
print(f"  Total Tax: ₹{tax_result['total_tax']:,.2f}")

# Test 3: Calculate Effective Rate
effective_rate = calculator.calculate_effective_rate(
    tax_result['total_tax'], 
    taxable_income
)
print(f"  Effective Rate: {effective_rate:.2f}%")

# ============================================================================
## 6. MANUAL TESTING - Deduction Calculator
# ============================================================================

from src.calculations.deductions import DeductionCalculator, DeductionSection

# Test 1: Create Deduction Calculator
ded_calc = DeductionCalculator()
print("✓ Deduction Calculator Initialized")

# Test 2: Add Deductions
ded_calc.add_deduction("80C", 150000, "Life Insurance")
ded_calc.add_deduction("80C", 50000, "PPF")
ded_calc.add_deduction("80D", 50000, "Medical Insurance")
print("✓ Deductions Added")

# Test 3: Get Deduction Summary
summary = ded_calc.get_deduction_summary()
print("✓ Deduction Summary:")
for section, details in summary.items():
    if details['claimed'] > 0:
        print(f"  {section}:")
        print(f"    Claimed: ₹{details['claimed']:,.2f}")
        print(f"    Limit: ₹{details['limit']:,.2f}")
        print(f"    Remaining: ₹{details['remaining']:,.2f}")

# Test 4: Validate Deduction
is_valid = ded_calc.validate_deduction("80C", 150000)
print(f"✓ Deduction Validation: {is_valid}")

# ============================================================================
## 7. MANUAL TESTING - Validators
# ============================================================================

from src.utils.validators import FormValidator

# Test PAN Validation
is_valid, msg = FormValidator.validate_pan("AAAAA0000A")
print(f"✓ PAN Validation: {msg}")

# Test Email Validation
is_valid, msg = FormValidator.validate_email("john@example.com")
print(f"✓ Email Validation: {msg}")

# Test Phone Validation
is_valid, msg = FormValidator.validate_phone("9876543210")
print(f"✓ Phone Validation: {msg}")

# Test Financial Year Validation
is_valid, msg = FormValidator.validate_financial_year("2023-24")
print(f"✓ Financial Year Validation: {msg}")

# ============================================================================
## 8. ERROR TESTING (Expected Failures)
# ============================================================================

# Test 1: Invalid PAN
try:
    PersonalDetails(
        pan="INVALID",  # Too short
        full_name="Test",
        date_of_birth=date(1990, 1, 1),
        address="Test",
        phone="9876543210",
        email="test@test.com"
    )
except ValueError as e:
    print(f"✓ Expected Error (Invalid PAN): {e}")

# Test 2: Negative Income
try:
    IncomeSource(
        income_type=IncomeType.SALARY,
        amount=-1000  # Negative amount
    )
except ValueError as e:
    print(f"✓ Expected Error (Negative Income): {e}")

# Test 3: Form Not Initialized
try:
    agent = ITR4Agent()
    agent.add_income({"income_type": "salary", "amount": 1000000})
except ValueError as e:
    print(f"✓ Expected Error (Form Not Initialized): {e}")

# ============================================================================
## 9. RUNNING PYTEST TESTS
# ============================================================================

# Create test file: tests/test_itr4_complete.py
# Then run: pytest tests/test_itr4_complete.py -v

# ============================================================================
## 10. COVERAGE REPORT
# ============================================================================

# Generate HTML coverage report
pytest tests/ --cov=src --cov-report=html

# View report
# Open htmlcov/index.html in your browser

# ============================================================================
## 11. CONTINUOUS INTEGRATION (GitHub Actions)
# ============================================================================

# Tests run automatically on:
# - Push to main/develop branches
# - Pull requests
# View results in: https://github.com/Arsh28786/itr4-agent/actions

# ============================================================================
## 12. QUICK TEST CHECKLIST
# ============================================================================

TEST_CHECKLIST = """
☐ Data Models (Forms)
  ☐ PersonalDetails creation and validation
  ☐ IncomeSource creation with validation
  ☐ Deduction creation with validation
  ☐ ITR4Form initialization
  ☐ Form total calculations

☐ Agent Functionality
  ☐ Agent initialization
  ☐ Interview start
  ☐ Form creation
  ☐ Add income
  ☐ Add deduction
  ☐ Get form summary
  ☐ Generate form
  ☐ Export form (JSON, XML, PDF)

☐ Calculations
  ☐ Tax calculation (income slab)
  ☐ Surcharge calculation
  ☐ Cess calculation
  ☐ Effective tax rate
  ☐ Deduction validation
  ☐ Deduction limits

☐ Validators
  ☐ PAN validation
  ☐ Email validation
  ☐ Phone validation
  ☐ Aadhaar validation
  ☐ Financial year validation

☐ Error Handling
  ☐ Invalid inputs
  ☐ Negative amounts
  ☐ Form not initialized
  ☐ Missing required fields
"""

print(TEST_CHECKLIST)
