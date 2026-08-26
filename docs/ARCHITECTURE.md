# ITR4 Agent Architecture

## Overview

The ITR4 Agent follows a modular architecture designed for extensibility, maintainability, and scalability.

## System Components

### 1. **Agent Module** (`src/agent/`)
- **itr4_agent.py**: Main agent orchestrator
  - Manages conversation flow
  - Coordinates form creation and data collection
  - Handles user interactions
- **conversational_flow.py**: Dialogue state management
  - Question sequencing
  - Context tracking

### 2. **Forms Module** (`src/forms/`)
- **itr4_model.py**: Data models
  - `ITR4Form`: Complete form structure
  - `PersonalDetails`: Taxpayer information
  - `IncomeSource`: Income data
  - `Deduction`: Deduction information
  
Uses Pydantic for validation and serialization.

### 3. **Calculations Module** (`src/calculations/`)
- **tax_calculator.py**: Tax computation
  - Tax slab calculation
  - Surcharge computation
  - Health and Education Cess
- **deductions.py**: Deduction management
  - Deduction limits validation
  - Section-wise calculations

### 4. **Generators Module** (`src/generators/`)
- **xml_generator.py**: XML output generation
  - ITR4 XML format compliance
  - File export
- **pdf_generator.py** (future): PDF generation
  - Formatted PDF output
  - Print-ready forms

### 5. **Utils Module** (`src/utils/`)
- **validators.py**: Input validation
  - PAN, Email, Phone validation
  - Financial year format checking
- **helpers.py**: Utility functions
  - Currency formatting
  - Date parsing
  - Financial year calculations

## Data Flow

```
User Input
    ↓
Agent Interview
    ↓
Form Creation (PersonalDetails)
    ↓
Income Collection
    ↓
Deduction Collection
    ↓
Tax Calculation
    ↓
Validation
    ↓
Form Generation (XML/PDF)
    ↓
Output Export
```

## Key Design Patterns

### 1. **Separation of Concerns**
Each module handles specific responsibilities:
- Data models are independent of business logic
- Calculations are separate from form structure
- Generation is separate from computation

### 2. **Validation at Entry Points**
- Pydantic models validate data on creation
- Custom validators for domain-specific rules
- Early error detection

### 3. **Immutability where Possible**
- Form data is structured and validated
- Changes trigger recalculation of totals

### 4. **Extensibility**
- Plugin architecture for calculations (future)
- Support for multiple output formats
- Configurable tax rules

## Extension Points

### Adding New Income Types
1. Add to `IncomeType` enum in `forms/itr4_model.py`
2. Update validation logic in `utils/validators.py`
3. Update calculator logic in `calculations/tax_calculator.py`

### Adding New Deduction Sections
1. Add to `DeductionSection` enum in `calculations/deductions.py`
2. Update `DEDUCTION_LIMITS` with new limits
3. Update calculation logic as needed

### Supporting New Output Formats
1. Create new generator class in `generators/`
2. Implement format-specific serialization
3. Add export method to `ITR4Agent`

## Configuration

Tax rules and rates are defined in:
- `src/calculations/tax_calculator.py`: Tax slabs and rates
- `src/calculations/deductions.py`: Deduction limits
- `config/tax_rules.json`: Externalized rules (future)

## Performance Considerations

1. **Lazy Calculation**: Tax calculations only performed when needed
2. **Caching**: Repeated calculations cached (future)
3. **Streaming**: Large form data can be streamed (future)

## Testing Strategy

- **Unit Tests**: Individual component testing
- **Integration Tests**: Component interaction testing
- **Validation Tests**: Input validation testing
- **End-to-End Tests**: Complete workflow testing
