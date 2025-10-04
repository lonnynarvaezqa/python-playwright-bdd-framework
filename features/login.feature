Feature: Secure Login Functionality

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters "tomsmith" as username and "SuperSecretPassword!" as password
    And the user clicks the login button
    Then the user should be redirected to the secure area
    And a message containing "You logged into a secure area!" should be displayed

  Scenario: Failed login due to invalid username
    Given the user is on the login page
    When the user enters "usuario_invalido" as username and "SuperSecretPassword!" as password
    And the user clicks the login button
    Then a message containing "Your username is invalid!" should be displayed

  Scenario: Failed login due to empty password field
    Given the user is on the login page
    When the user enters "tomsmith" as username and "empty_value" as password
    And the user clicks the login button
    Then a message containing "Your password is invalid!" should be displayed

  Scenario: Logout functionality returns user to login page
    Given the user is logged in
    When the user clicks the logout button
    Then the user should be on the login page
    And a message containing "You logged out of the secure area!" should be displayed

  Scenario: Password input field should mask characters
    Given the user is on the login page
    Then the password input field should have type "password"

  Scenario: Direct access to secure area without credentials should fail
    Given the user is on the login page
    When the user attempts to navigate directly to "/secure"
    Then the user should be on the login page
    And a message containing "You must login to view the secure area!" should be displayed
