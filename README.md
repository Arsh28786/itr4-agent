# ITR4 Agent

An intelligent agent for filling and generating ITR4 (Income Tax Return) forms for Indian taxpayers.

## Overview

This project aims to automate the process of collecting taxpayer information and generating compliant ITR4 forms for submission to the Indian Income Tax Department.

## Features

- **Conversational Interface**: Agent-based Q&A to collect taxpayer information
- **Form Validation**: Ensures all data complies with ITR4 requirements
- **Tax Calculations**: Automatic computation of taxable income, deductions, and tax liability
- **Form Generation**: Generates ITR4 XML/PDF output
- **Multi-Source Income Support**: Handles salary, business, capital gains, and other income sources
- **Deduction Management**: Automatically applies standard and itemized deductions

## Project Structure

```
itr4-agent/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── itr4_agent.py
│   │   └── conversational_flow.py
│   ├── forms/
│   │   ├── __init__.py
│   │   └── itr4_model.py
│   ├── calculations/
│   │   ├── __init__.py
│   │   ├── tax_calculator.py
│   │   └── deductions.py
│   ├── generators/
│   │   ├── __init__.py
│   │   ├── xml_generator.py
│   │   └── pdf_generator.py
│   └── utils/
│       ├── __init__.py
│       ├── validators.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_agent.py
│   ├── test_calculator.py
│   └── test_generators.py
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── ITR4_GUIDE.md
└── config/
    ├── tax_rules.json
    └── settings.py
```

## Tech Stack

- **Backend**: Python 3.9+
- **Agent Framework**: LangChain / Custom Rule Engine
- **LLM Integration**: OpenAI GPT or Claude (optional)
- **Data Validation**: Pydantic
- **Form Generation**: ReportLab (PDF), XML libraries
- **Testing**: pytest

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Arsh28786/itr4-agent.git
   cd itr4-agent
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```python
from src.agent.itr4_agent import ITR4Agent

# Initialize the agent
agent = ITR4Agent()

# Start the conversational flow
agent.start_interview()

# Generate ITR4 form
itr4_form = agent.generate_form()

# Export as XML or PDF
agent.export_form(format='xml', filename='itr4_output.xml')
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## Disclaimer

⚠️ **Important**: This tool is for educational and informational purposes. Always consult with a qualified tax professional or Chartered Accountant before filing your ITR. The authors are not responsible for any errors in tax calculations or form submission.

## License

MIT License - See LICENSE file for details

## Resources

- [Income Tax Department Official Website](https://www.incometaxindia.gov.in/)
- [ITR4 Form Guide](https://www.incometaxindia.gov.in/)
- [Tax Rules and Regulations](https://www.incometaxindia.gov.in/)

## Support

For issues or questions, please open an issue on GitHub.

---

**Last Updated**: 2026-08-26
