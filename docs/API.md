# ITR4 Agent API Documentation

## Core Classes

### ITR4Agent

Main agent for managing ITR4 form filling.

#### Methods

##### `__init__()`
Initialize a new ITR4Agent instance.

```python
agent = ITR4Agent()
```

##### `start_interview() -> str`
Begin the conversational interview process.

```python
welcome_message = agent.start_interview()
```

Returns: Welcome message and first question.

##### `process_user_input(user_input: str) -> str`
Process user response and generate next question.

```python
response = agent.process_user_input("My PAN is AAAAA0000A")
```

##### `create_form(personal_details: Dict[str, Any]) -> ITR4Form`
Create a new ITR4 form with personal details.

```python
form = agent.create_form({
    "pan": "AAAAA0000A",
    "full_name": "John Doe",
    "date_of_birth": "1990-01-15",
    "address": "123 Main St",
    "phone": "9876543210",
    "email": "john@example.com"
})
```

##### `add_income(income_data: Dict[str, Any])`
Add an income source to the form.

```python
agent.add_income({
    "income_type": "salary",
    "amount": 1000000,
    "description": "Annual salary"
})
```

##### `add_deduction(deduction_data: Dict[str, Any])`
Add a deduction to the form.

```python
agent.add_deduction({
    "name": "Life Insurance Premium",
    "amount": 150000,
    "section": "80C"
})
```

##### `get_form_summary() -> Dict[str, Any]`
Get a summary of current form data.

```python
summary = agent.get_form_summary()
# {
#   "pan": "AAAAA0000A",
#   "name": "John Doe",
#   "gross_income": 1000000,
#   "taxable_income": 850000,
#   ...
# }
```

##### `generate_form() -> ITR4Form`
Generate the final ITR4 form.

```python
itr4_form = agent.generate_form()
```

##### `export_form(format: str = 'json', filename: Optional[str] = None) -> str`
Export form in specified format.

```python
# Export as JSON
json_output = agent.export_form(format='json')

# Export as XML
xml_output = agent.export_form(format='xml')
```

---

## Data Models

### ITR4Form

Complete ITR4 form structure.

**Attributes:**
- `personal_details: PersonalDetails` - Taxpayer information
- `financial_year: str` - FY in format YYYY-YY
- `income_sources: List[IncomeSource]` - List of income sources
- `deductions: List[Deduction]` - List of deductions
- `gross_income: float` - Total income
- `total_deductions: float` - Total deductions
- `taxable_income: float` - Taxable income
- `tax_liability: float` - Tax to be paid

### PersonalDetails

Taxpayer personal information.

**Attributes:**
- `pan: str` - Permanent Account Number
- `full_name: str` - Full name
- `date_of_birth: date` - Date of birth
- `address: str` - Address
- `phone: str` - Phone number
- `email: str` - Email address
- `aadhaar: Optional[str]` - Aadhaar number (optional)

### IncomeSource

Income source information.

**Attributes:**
- `income_type: IncomeType` - Type of income (salary, business, etc.)
- `amount: float` - Income amount in INR
- `description: Optional[str]` - Description

### Deduction

Deduction information.

**Attributes:**
- `name: str` - Deduction name
- `amount: float` - Deduction amount in INR
- `section: str` - Income Tax Act section

---

## Utility Functions

### TaxCalculator

Calculate income tax based on taxable income.

```python
from src.calculations.tax_calculator import TaxCalculator

calculator = TaxCalculator(financial_year="2023-24")
result = calculator.calculate_tax(taxable_income=1000000)
# {
#   "taxable_income": 1000000,
#   "basic_tax": 150000,
#   "surcharge": 7500,
#   "cess": 6300,
#   "total_tax": 163800
# }
```

### DeductionCalculator

Manage and validate deductions.

```python
from src.calculations.deductions import DeductionCalculator

calc = DeductionCalculator()
calc.add_deduction("80C", 150000, "Life Insurance")

summary = calc.get_deduction_summary()
```

### FormValidator

Validate form inputs.

```python
from src.utils.validators import FormValidator

is_valid, message = FormValidator.validate_pan("AAAAA0000A")
is_valid, message = FormValidator.validate_email("user@example.com")
is_valid, message = FormValidator.validate_phone("9876543210")
```

---

## Example Usage

### Complete Workflow

```python
from src.agent.itr4_agent import ITR4Agent

# Initialize agent
agent = ITR4Agent()

# Start interview
print(agent.start_interview())

# Create form with personal details
agent.create_form({
    "pan": "AAAAA0000A",
    "full_name": "John Doe",
    "date_of_birth": "1990-01-15",
    "address": "123 Main St, City",
    "phone": "9876543210",
    "email": "john@example.com"
})

# Add income
agent.add_income({
    "income_type": "salary",
    "amount": 1000000,
    "description": "Annual salary"
})

# Add deductions
agent.add_deduction({
    "name": "Life Insurance Premium",
    "amount": 150000,
    "section": "80C"
})

# Get summary
summary = agent.get_form_summary()
print(summary)

# Generate and export
form = agent.generate_form()
xml_output = agent.export_form(format='xml')
print(xml_output)
```

---

## Error Handling

All methods validate inputs and raise appropriate exceptions:

- `ValueError`: Invalid input values
- `AttributeError`: Missing required attributes
- `TypeError`: Incorrect data types

Always wrap agent calls in try-except blocks for production use.
