# features/navigation.feature
Feature: General Site Navigation

  Scenario: Verify link navigation to the Horizontal Slider page
    Given the user is on the main landing page
    When the user clicks the link titled "Horizontal Slider"
    Then the user should be redirected to the URL containing "/horizontal_slider"
    And the page header should display "Horizontal Slider"

    Scenario Outline: Verify navigation and page header for multiple links
    Given the user is on the main landing page
    When the user clicks the link titled "<Link Text>"
    Then the user should be redirected to the URL containing "<Partial URL>"
    And the page header should display "<Header Text>"

    Examples: Links to verify
      | Link Text             | Partial URL         | Header Text           |
      | Checkboxes            | /checkboxes         | Checkboxes            |
      | Dropdown              | /dropdown           | Dropdown List         |
      | Context Menu          | /context_menu       | Context Menu          |
      | Key Presses           | /key_presses        | Key Presses           |
      | Dynamic Content       | /dynamic_content    | Dynamic Content       |
