# 📈 Test Strategy Document

## 1. Introduction
This document outlines the strategy for E2E automation testing using Python, Playwright, and the Behave BDD framework. The goal is to maximize test coverage of critical user paths while prioritizing code maintainability.

## 2. Test Approach
| Component | Technology / Method | Rationale |
| :--- | :--- | :--- |
| **Test Design** | Behavior-Driven Development (BDD) | Ensures alignment between business requirements and technical implementation. |
| **Code Structure** | Page Object Model (POM) + Separation of Locators | Decouples business logic from UI selectors, making tests resilient to UI changes. |
| **Execution** | Playwright (Chromium) | Modern tool supporting rapid, reliable, and multi-browser execution. |
| **Reporting** | Allure Report | Provides rich, interactive dashboards for clear reporting and failure analysis. |

## 3. Scope of Testing
The current scope focuses on **Functional E2E Testing** for core application flows, including:
* User Authentication (Login/Logout, Invalid Credentials).
* Navigation and URL Validation.
* Advanced Interactions (e.g., File Uploads).

## 4. Environment
* **Target Application:** The Internet Heroku App (https://the-internet.herokuapp.com)
* **OS:** Cross-platform (macOS, Linux, Windows)
* **Browser:** Chromium (for default execution)

## 5. Maintenance and Scalability
* Locators are centralized in `pages/elements/` files.
* Complex setups are abstracted using Behave's `@given` steps (e.g., "the user is logged in").
* Tests are run via a single script (`run_tests.sh`) to simplify execution and reporting.