# RESTful API Test Automation using Python, Pytest and Requests

This is a simple yet complete REST API test automation project built using **Python**, **Pytest**, and **Requests**.  
It tests the public API available at [restful-api.dev](https://restful-api.dev/) by covering the full lifecycle of an object: `POST`, `GET`, `PUT`, and `DELETE`.

---

## Project Structure

```
restful_api_tests/
├── data/
│   └── test_data.json         # Test input data
├── tests/
│   └── test_create_item.py    # Full item lifecycle test
├── utils/
│   └── api_client.py          # HTTP client wrapper
├── config/
│   └── config.py              # Base URL config
├── requirements.txt           # Project dependencies
├── pytest.ini                 # Pytest config
└── README.md
```

---

## Features

- End-to-end testing of REST endpoints (`POST`, `GET`, `PUT`, `DELETE`)
- Clean project structure for maintainability
- Uses external JSON file for test data
- Simple reusable API client wrapper
- Easily extendable for other endpoints or scenarios

---

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/lozal/api-tests-python-requests-01.git
   cd restful-api-tests
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶Running the Tests

Run all tests with:
```bash
pytest
```

Or run a specific test file:
```bash
pytest tests/test_create_item.py
```

Verbose output:
```bash
pytest -v -s
```

---


## Notes

- This project is for demonstration and educational purposes.
- It uses a public API from [restful-api.dev](https://restful-api.dev/) — no authentication required.
- Items created via this API are ephemeral and may be deleted over time.

---

## Technologies Used

- Python 3.10+
- Pytest
- Requests
- JSON
