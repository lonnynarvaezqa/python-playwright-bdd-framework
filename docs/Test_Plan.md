
# Test Plan: BDD Playwright Project

## Introduction and Objectives

This test plan outlines the scope, strategy, and execution details for the automated test suite developed using Python, Playwright, and Behave.

The primary objective of this repository is to serve as a **portfolio project for automation practice**, demonstrating robust E2E testing capabilities in a structured framework.

**Key Objectives:**

1.  **Validate E2E Flows:** Ensure critical user journeys (Login, Logout, File Upload) function correctly.
    
2.  **Ensure Code Quality:** Demonstrate implementation of best practices, including POM and Locator Separation.
    
3.  **Produce Professional Reports:** Generate clear, detailed, and actionable results using Allure Report.
    

## Scope


| In Scope                                   | Out of Scope                      |
|--------------------------------------------|------------------------------------|
| Functional E2E Testing (Happy/Unhappy Paths)| Performance Testing (Load/Stress)  |
| UI Validation (Input types, visibility)    | Security Penetration Testing       |
| Session Management (Login/Logout/Direct Access) | Accessibility Testing (A11y)   |
| Navigation and URL Redirection             | Multi-language/Localization Testing|


## Test Strategy

The test strategy employs **Behavior-Driven Development (BDD)** to define executable specifications. This ensures maximum alignment between business expectations (Gherkin in `.feature` files) and the technical implementation (Python steps and POM).

1.  **Design Pattern:**  **Page Object Model (POM)** with **Separation of Locators** (`pages/elements/`) for high maintainability.
    
2.  **Tooling:** Playwright is used for its modern API, reliability, and auto-waiting capabilities.
    
3.  **Data Management:** Test data is managed in the `test_data/` directory. For example, a dummy file is used for the File Upload test case.
    
4.  **Reporting:** All tests generate intermediate results for **Allure Report**, providing interactive dashboards for failure analysis and status tracking.
    

## Test Environment


| Component            | Detail                           | Notes                                                                 |
|-----------------------|----------------------------------|----------------------------------------------------------------------|
| Target Application    | The Internet Heroku App          | Stable, publicly available testing environment.                      |
| Browsers              | Chromium (Default)               | Tests are written to be cross-browser compatible (Playwright default).|
| Execution Environment | Python 3.9+ Virtual Environment (.venv) | Local execution (on-demand).                                 |
| CI Integration        | Not implemented (Manual execution) | Designed for easy integration into CI/CD pipelines (e.g., Jenkins, GitHub Actions). |


## Resources and Responsibilities


| Role                  | Responsibility                                                                 |
|------------------------|--------------------------------------------------------------------------------|
| Automation Engineer (You) | Test implementation, debugging, framework maintenance, documentation, and report generation. |
| Reviewer/Interviewer   | Review of test strategy and analysis of final Allure Reports.                  |


## Deliverables

1.  **Executable Test Suite:** All `.feature` files and supporting Python code.
    
2.  **Allure Report:** Automatically generated HTML report reflecting the latest test run.
    
3.  **Documentation (`docs/`):** Test Strategy, Test Plan, and Test Cases List.
    
4.  **GitHub Repository:** Structured and version-controlled codebase.
    

## Communication Plan

All communication regarding test status, failures, and coverage metrics will be managed through the **Allure Report dashboard**, which provides a single source of truth for the test execution results.