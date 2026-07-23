# QA Automation Projects

A collection of automated test suites built using Python, Selenium, and Pytest following the Page Object Model (POM) design pattern.

## 🧪 Test Suites

### 1. Books Page Tests — `tests/test_books_pom.py`
Automated tests for books.toscrape.com using Page Object Model.
- Verifies page title loads correctly
- Verifies books are visible on the page
- Verifies price is displayed correctly

### 2. Login Page Tests — `tests/test_login.py`
Automated login flow tests for quotes.toscrape.com.
- Valid login test
- Empty credentials test
- Post-login verification using Logout button

### 3. Basic Pytest Tests — `tests/test_first.py`
Introduction to pytest — unit tests for basic Python functions.
- Addition function tests
- Positive, negative, and zero cases

### 4. Browser Tests — `tests/test_browser.py`
Direct browser automation tests without POM.
- Page title verification
- Element visibility checks
- Content validation

## 📁 Project Structure

```
QA/
├── pages/
│   ├── books_page.py      ← Books page object
│   └── login_page.py      ← Login page object
├── tests/
│   ├── test_books_pom.py  ← Books page tests
│   ├── test_login.py      ← Login flow tests
│   ├── test_first.py      ← Basic pytest tests
│   └── test_browser.py    ← Browser automation tests
├── report.html            ← Generated HTML test report
└── README.md
```

## Setup

```bash
git clone https://github.com/heyridham7/qa-automation-projects.git
cd qa-automation-projects
python3 -m venv venv
source venv/bin/activate
pip install pytest selenium webdriver-manager pytest-html
```

## Running Tests

```bash
# Run all tests
pytest tests/ -v

# Run with HTML report
pytest tests/ -v --html=report.html --self-contained-html

# Run specific test file
pytest tests/test_login.py -v
```

## Tech Stack

- Python 3
- Selenium WebDriver — browser automation
- Pytest — test framework
- pytest-html — HTML test reports
- webdriver-manager — automatic ChromeDriver management
- Page Object Model (POM) — design pattern for maintainable tests
